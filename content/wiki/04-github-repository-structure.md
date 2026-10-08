---
title: GitHub repository structure
category: Research practice
order: 5
summary: Standard structure for lab project repositories.
updated: 2026-10-08
---

# GitHub repository structure

Each research project should have its own repository in the [Zarkali Lab GitHub organisation](https://github.com/Zarkali-lab), created from the lab `project-template`.

Shared preprocessing or analysis pipelines used across projects belong in the relevant shared repository (for example `fmri` or `diffusion`), rather than being copied into each project.

## Project repository

Use this structure:

```text
project/
├── README.md
├── docs/
│   ├── data_dictionary.md
│   ├── qc.md
│   ├── decisions/
│   ├── experiments/
│   └── meetings/
├── config/
├── scripts/
├── src/
├── notebooks/
└── manuscript/
```

Not every folder needs to be used. Add files only when useful.

## What goes where

- **README:** main project record — question, hypotheses, team, cohorts, data locations, how analysis runs, software and outputs.
- **data_dictionary.md:** variable definitions and coding.
- **qc.md:** project QC criteria and brief notes.
- **experiments:** analyses/tests worth preserving beyond code itself.
- **decisions:** important choices where rationale may matter later.
- **meetings:** brief notes, decisions and actions.
- **config:** non-sensitive parameters and example paths.
- **scripts / src / notebooks:** analysis code.
- **manuscript:** manuscript-related material where appropriate.

## Rules

1. Start new projects from `project-template`.
2. Keep project context in README; avoid duplicate documentation.
3. Keep documentation minimal — record only information that will be useful later.
4. Do not commit identifiable participant data, raw scans, credentials or sensitive clinical data.
5. Keep shared/reusable pipelines in shared lab repositories and record version or commit used by project.
6. Use GitHub Issues for tasks; use experiment/decision records only when result or rationale is worth retaining.
