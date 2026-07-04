# Target Core Architecture (V2)

This document describes the decoupled architectural design (V2) of the content automation pipeline.

## System Layout (V2)

```
┌────────────────────────────────────────────────────────┐
│                     CLIENT / CRON                      │
└───────────────────────────┬────────────────────────────┘
                            │ Instantiates & triggers runs
                            ▼
┌────────────────────────────────────────────────────────┐
│                   ABSTRACT ENGINE                      │
│ Uses interfaces: ResearchProvider, ContentGenerator,   │
│                  AssetGenerator, Publisher, Scheduler  │
└───────────────────────────┬────────────────────────────┘
                            │ Calls implementations at runtime
                            ▼
┌────────────────────────────────────────────────────────┐
│                    PLATFORM ADAPTERS                   │
│  - LinkedIn Adapter:                                   │
│    Uses schedule_all_posts.cjs, html layouts, prompts  │
│  - Instagram Adapter (Future):                         │
│    Uses custom posting scripts and ZIP image carousels │
└────────────────────────────────────────────────────────┘
```

---

## Component Separation Details

### 1. Interface Decoupling
The core pipeline is platform-independent. It interacts with services only through abstract interfaces (e.g. `ResearchProvider`, `ContentGenerator`, `Publisher`). Platform-specific behaviors are isolated inside adapters (such as `adapters/linkedin/` or a future `adapters/instagram/`).

### 2. Standardized Configuration
Both Python and Node.js components load environment variables and system paths from centralized config files ([core/config/config.py](file:///Users/anny/Downloads/Archives/instagram/core/config/config.py) and [core/config/config.cjs](file:///Users/anny/Downloads/Archives/instagram/core/config/config.cjs)) rather than manually parsing the `.env` file across multiple scripts.

### 3. Reusable Visual Pipelines
HTML rendering and screenshotting scripts generate platform-agnostic output files (PNGs and PDFs) inside the local file system. The publishers and schedulers then take these output assets and deliver them to their respective destination channels (Slack, LinkedIn, or Instagram).
