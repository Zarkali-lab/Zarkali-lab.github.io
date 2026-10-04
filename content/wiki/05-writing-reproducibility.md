---
title: Writing & reproducibility
category: Research practice
order: 6
summary: Figures, manuscripts, analysis records and review habits.
updated: 2026-10-01
---

# Writing & reproducibility

## Figures first

A strong analysis should be explainable through a small set of figures. Keep scripts that produce final figures in the repository and avoid manual cosmetic changes that cannot be reproduced.

## Manuscripts

Use descriptive filenames or version control rather than chains such as `final_v7_reallyfinal.docx`.

Before internal review, check:

- sample counts agree across abstract, methods, tables and figures
- statistical tests match stated hypotheses
- abbreviations are defined once and used consistently
- figure legends can be understood without reading main text
- code and analysis notes identify the exact outputs used

## Decisions

Record material analysis decisions in issues, pull requests, a changelog or structured notes. Future-you should be able to answer *why did we do this?*
