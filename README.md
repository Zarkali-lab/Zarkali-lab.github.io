# Zarkali Lab website

Custom static research-lab website + Markdown wiki. Configured for GitHub Pages.

## What is included

- responsive public site: Home, Research, People, Join us, Publications
- searchable Wiki tab
- wiki articles written in plain Markdown
- light/dark theme
- no frontend framework or JS dependency
- small Python build script using Jinja2 + Mistune

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

Research, people, join, publications and news:

```text
content/research.yml
content/people.yml
content/join.yml
content/publications.yml
content/news.yml
```

Wiki pages:

```text
content/wiki/*.md
```

## Publish with GitHub Pages

For the organisation root URL:

```text
https://zarkali-lab.github.io
```

this repository must be named:

```text
Zarkali-lab.github.io
```

The workflow in `.github/workflows/pages.yml` automatically detects an organisation/user Pages repository and builds with an empty base path, so internal links and assets resolve from the domain root.

After renaming the repository:

1. Open repository **Settings → Pages**.
2. Under **Build and deployment**, set **Source** to **GitHub Actions**.
3. Push to `main`, or run the Pages workflow manually from **Actions**.

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
