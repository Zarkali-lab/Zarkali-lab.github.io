# Zarkali Lab website

Custom static research-lab website + Markdown wiki. Designed for GitHub Pages.

## What is included

- responsive public site: Home, Research, People, Publications
- searchable Wiki tab
- wiki articles written in plain Markdown
- light/dark theme
- no frontend framework or JS dependency
- small Python build script using Jinja2 + Mistune
- GitHub Pages deployment workflow
- automatic support for `username.github.io/repository/` project paths

## Local preview

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
python build.py
python -m http.server 8000 -d dist
```

Open `http://localhost:8000`.

## Edit content

Main site settings:

```text
site.yml
```

Research, people, publications and news:

```text
content/research.yml
content/people.yml
content/publications.yml
content/news.yml
```

Wiki pages:

```text
content/wiki/*.md
```

Add a wiki file with frontmatter:

```md
---
title: Example page
category: Research practice
order: 20
summary: One-sentence description.
updated: 2026-10-01
---

# Example page

Your Markdown here.
```

## Publish on GitHub Pages

1. Create GitHub repository and copy this project into it.
2. Push to `main`.
3. In repository: **Settings → Pages → Build and deployment → Source → GitHub Actions**.
4. Workflow in `.github/workflows/pages.yml` builds and deploys site.

For custom domain, configure it in GitHub Pages settings. Add `CNAME` handling to workflow if you want domain stored in repo.

## Design notes

Public-facing structure takes cues from modern academic lab sites, while wiki uses a denser documentation layout. Visual system is original: editorial typography, scientific network motif, strong spacing, minimal editorial layout, restrained blue accent and low-dependency interaction.

## Project concept images and funder logos

Current and past research projects use the same fields in `content/research.yml`.
Place image assets in `assets/img/`, then reference them from a project:

```yaml
concept_image: /assets/img/my-project.jpg
concept_alt: Description of the research concept image
funder_logo: /assets/img/funder-logo.svg
funder_name: Parkinson's UK
```

Leave either image path blank to show the neutral placeholder slot. `past_projects` accepts the same structure as `areas` (current projects).
