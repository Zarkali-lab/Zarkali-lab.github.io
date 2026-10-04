---
title: Imaging workflows
category: Research practice
order: 5
summary: Conventions for MRI, PET and multimodal image analysis.
updated: 2026-10-01
---

# Imaging workflows

## Keep stages explicit

Prefer pipelines with clear boundaries between raw data, preprocessing, quality control, feature extraction and statistical analysis.

```text
raw → conversion/BIDS → preprocessing → QC → derivatives → statistics → figures
```

## Quality control

Automated QC is useful but never a substitute for visual inspection. Record exclusions and reruns in a machine-readable table with reason, date and reviewer where practical.

## Registration

Always inspect transformed images rather than trusting command success. For group analyses, document interpolation, reference space and any masks used.

## Multimodal work

When combining MRI, PET, MRSI or clinical measures, define the spatial and temporal unit of analysis before modelling. Avoid silent resampling chains; retain provenance for derived maps.
