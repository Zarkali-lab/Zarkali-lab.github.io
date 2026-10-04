---
title: Data & code
category: Research practice
order: 4
summary: Version control, data separation, naming and reproducible analysis.
updated: 2026-10-01
---

# Data & code

## Core rule

Code is versioned. Raw research data is not placed in Git unless a dataset is explicitly public, non-sensitive and suitable for repository storage.

## Suggested project shape

```text
project/
├── README.md
├── pyproject.toml
├── config/
├── src/
├── scripts/
├── tests/
├── notebooks/
├── derivatives/   # generated, usually ignored
└── docs/
```

## Reproducibility

- pin important dependencies
- record software versions used in published analysis
- prefer scripted transformations over manual edits
- keep parameters in config files when practical
- make output regeneration possible from documented inputs
- write tests for reusable code and fragile data transforms

## Notebooks

Good for exploration and communication. Move stable analysis logic into functions or scripts once it becomes part of a pipeline.
