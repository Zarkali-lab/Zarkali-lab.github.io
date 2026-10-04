# Zarkali Lab website

Custom static research-lab website + Markdown wiki. Configured for GitHub Pages.

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
