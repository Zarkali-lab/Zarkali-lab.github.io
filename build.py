#!/usr/bin/env python3
from __future__ import annotations

import argparse
import html
import re
import shutil
from datetime import datetime
from pathlib import Path

import mistune
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).resolve().parent
CONTENT = ROOT / "content"
TEMPLATES = ROOT / "templates"
ASSETS = ROOT / "assets"
DIST = ROOT / "dist"


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def slugify(value: str) -> str:
    value = re.sub(r"[^a-zA-Z0-9\s-]", "", value).strip().lower()
    return re.sub(r"[-\s]+", "-", value)


def parse_frontmatter(path: Path):
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", text, re.S)
    if not match:
        raise ValueError(f"Missing YAML frontmatter: {path}")
    meta = yaml.safe_load(match.group(1)) or {}
    return meta, match.group(2)


def human_date(value) -> str:
    if hasattr(value, "strftime"):
        return value.strftime("%d %b %Y")
    try:
        return datetime.strptime(str(value), "%Y-%m-%d").strftime("%d %b %Y")
    except ValueError:
        return str(value)


def add_heading_ids(markdown_text: str):
    toc = []
    seen = {}

    def repl(match):
        level = len(match.group(1))
        text = match.group(2).strip()
        plain = re.sub(r"[*_`~]", "", text)
        base = slugify(plain) or "section"
        seen[base] = seen.get(base, 0) + 1
        ident = base if seen[base] == 1 else f"{base}-{seen[base]}"
        if level == 2:
            toc.append({"id": ident, "text": plain})
        return f'<h{level} id="{ident}">{html.escape(plain)}</h{level}>'

    transformed = re.sub(r"^(#{1,3})\s+(.+)$", repl, markdown_text, flags=re.M)
    return transformed, toc


def main():
    parser = argparse.ArgumentParser(description="Build Zarkali Lab static site")
    parser.add_argument("--base-path", default=None, help="GitHub Pages project path, e.g. /zarkali-lab")
    args = parser.parse_args()

    site = load_yaml(ROOT / "site.yml")
    base_path = args.base_path if args.base_path is not None else site.get("base_path", "")
    base_path = ("/" + base_path.strip("/")) if base_path and base_path != "/" else ""
    site["base_path"] = base_path

    def url(path: str) -> str:
        if path.startswith(("http://", "https://", "mailto:", "#")):
            return path
        path = "/" + path.lstrip("/")
        return f"{base_path}{path}"

    env = Environment(
        loader=FileSystemLoader(TEMPLATES),
        autoescape=select_autoescape(["html", "xml"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.globals.update(url=url, year=datetime.now().year)

    research = load_yaml(CONTENT / "research.yml")
    people = load_yaml(CONTENT / "people.yml")
    publications = load_yaml(CONTENT / "publications.yml")
    news = load_yaml(CONTENT / "news.yml")
    join = load_yaml(CONTENT / "join.yml")

    wiki = []
    renderer = mistune.HTMLRenderer(escape=False)
    markdown = mistune.create_markdown(renderer=renderer, plugins=["strikethrough", "table", "task_lists"])
    join = {key: markdown(value or "") for key, value in join.items()}

    for path in sorted((CONTENT / "wiki").glob("*.md")):
        meta, body = parse_frontmatter(path)
        slug = re.sub(r"^\d+-", "", path.stem)
        transformed, toc = add_heading_ids(body)
        category = meta.get("category", "General")
        wiki.append({
            **meta,
            "slug": slug,
            "category": category,
            "category_slug": slugify(category),
            "updated_human": human_date(meta.get("updated", "")),
            "content": markdown(transformed),
            "toc": toc,
        })
    wiki.sort(key=lambda p: (p.get("order", 999), p["title"]))

    counts = {}
    for page in wiki:
        counts[page["category"]] = counts.get(page["category"], 0) + 1
    categories = [{"name": k, "slug": slugify(k), "count": v} for k, v in counts.items()]

    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True)
    shutil.copytree(ASSETS, DIST / "assets")
    (DIST / ".nojekyll").write_text("", encoding="utf-8")

    common = dict(site=site, research=research, people=people, publications=publications, news=news, join=join, wiki=wiki, categories=categories)

    pages = [
        ("home.html", DIST / "index.html", {"title": None, "active_nav": "Home", "page_key": "home"}),
        ("research.html", DIST / "research" / "index.html", {"title": "Research", "active_nav": "Research", "page_key": "research"}),
        ("people.html", DIST / "people" / "index.html", {"title": "People", "active_nav": "People", "page_key": "people"}),
        ("join.html", DIST / "join" / "index.html", {"title": "Join us", "active_nav": "Join us", "page_key": "join"}),
        ("publications.html", DIST / "publications" / "index.html", {"title": "Publications", "active_nav": "Publications", "page_key": "publications"}),
        ("wiki_index.html", DIST / "wiki" / "index.html", {"title": "Wiki", "active_nav": "Wiki", "page_key": "wiki"}),
    ]

    for template_name, out, extra in pages:
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(env.get_template(template_name).render(**common, **extra), encoding="utf-8")

    article_template = env.get_template("wiki_article.html")
    for page in wiki:
        out = DIST / "wiki" / page["slug"] / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(article_template.render(
            **common,
            title=page["title"],
            active_nav="Wiki",
            page_key="wiki-article",
            page=page,
            content=page["content"],
            toc=page["toc"],
            page_description=page.get("summary"),
        ), encoding="utf-8")

    print(f"Built {len(pages) + len(wiki)} pages → {DIST}")
    if base_path:
        print(f"Base path: {base_path}")


if __name__ == "__main__":
    main()
