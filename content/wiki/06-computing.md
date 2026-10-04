---
title: Computing & HPC
category: Technical
order: 7
summary: SSH, environments, jobs and shared compute etiquette.
updated: 2026-10-01
---

# Computing & HPC

## SSH

Use SSH keys rather than passwords where supported. Keep private keys private and protect them with an appropriate passphrase.

## Cluster jobs

Do not run heavy analysis on login nodes. Use scheduler jobs for CPU-, memory- or GPU-intensive work and request resources that reflect measured need.

## Environments

Keep environment setup reproducible. For Python, prefer `pyproject.toml` plus lockfile or an environment specification appropriate to the project.

## Storage

Scratch space is temporary. Project storage is not a backup by default. Know which tier is backed up before relying on it.
