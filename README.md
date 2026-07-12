# Multi-Platform Content Automation

> A configurable automation platform for researching, generating, assembling, and scheduling branded content across LinkedIn and Instagram.

This project is an operations-focused content pipeline. It collects signals from configurable sources, turns selected topics into platform-specific copy and visual briefs, renders assets, and hands approved content to publishing adapters.

## Capabilities

- Configurable research across community, news, and performance signals.
- LLM-assisted LinkedIn and Instagram content generation.
- Niche- and brand-aware campaign configuration.
- Carousel and infographic asset compilation.
- Platform-specific publishing and scheduling adapters.
- Slack-oriented delivery/approval hooks and operational utilities.

## Design

```text
Research sources
      │
      ▼
Topic intelligence → content generation → visual compiler → publishing adapters
      │                    │                    │                 ├── LinkedIn
      │                    │                    │                 └── Instagram
      └──────── configuration, prompts, validation and analytics ──┘
```

## Repository layout

```text
core/
  research/                # source and topic intelligence
  content/                 # platform-aware content generation
  visuals/                 # asset/visual composition
  publishing/              # workflow-facing publishing code
  config/                  # campaign and niche configuration
adapters/
  linkedin/ instagram/     # external-platform implementations
carousel-routine/          # rendering utilities
commands/ prompts/         # operational commands and versioned prompt assets
```

## Prerequisites

- Python 3.10+
- Node.js 18+
- An approved LLM provider and any configured third-party platform credentials

Keep credentials only in `.env` files and use the least-privilege scopes required by each adapter. Never hard-code API keys or platform tokens.

## Local setup

Install the JavaScript dependencies used by the rendering workflow:

```bash
cd carousel-routine
npm install
```

Review `core/config/` and each publishing adapter before running workflows. Start with a dry-run or locally rendered asset; external scheduling and publishing should be an explicit, separately authorized operation.

## Engineering direction

This repository contains valuable working automation but has accumulated one-off scripts from rapid iteration. The active refactor will establish a single supported CLI, move legacy/datelike scripts out of the project root, add typed workflow contracts, and test adapter payloads and rendered artifacts.

## Status

Active portfolio project. The intended public story is a safe, configurable automation system—not a collection of ad hoc scripts.
