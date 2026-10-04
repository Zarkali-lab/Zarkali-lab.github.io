---
title: Data & code
category: Research practice
order: 4
summary: Version control, data separation, naming and reproducible analysis.
updated: 2026-10-01
---

# Sharing results and code

## Results & Authorships
Like other labs, we will follow the APA guidelines with respect to authorship:

_“Authorship credit should reflect the individual’s contribution to the study.”_

At the start of a new project we will discuss authorship. Angelika will typically be the last author and the person leading the project will typically be the first author. Authorship will primarily reflect the contribution to the project. We will try to make this clear in advance so no surprises occur, but if authorship needs to be updated at a later stage because, for example, somebody leaves and roles change, this will be discussed explicitly at that time.

## Code: the lab github

All analysis code for projects in the lab should be kept within the lab github repository.
Code should be versioned. Raw research data is not placed in Git unless a dataset is explicitly public, non-sensitive and suitable for repository storage.
All pipelines for preprocessing and analysis that are used across different projects should be added to the relevant github repo. 
For all individual projects, you should create a new repo (this could be initially private) within the projects/ folder. 
This will be published together with the journal publication so bear that in mind. 

### Suggested project shape

```text
project/
├── README.md
├── config/
├── scripts/
├── tests/
├── notebooks/
├── derivatives/   # generated, usually ignored
└── docs/
```

### Reproducibility principles

- pin important dependencies
- record software versions used in published analysis
- prefer scripted transformations over manual edits
- keep parameters in config files when practical
- make output regeneration possible from documented inputs
- write tests for reusable code and fragile data transforms
