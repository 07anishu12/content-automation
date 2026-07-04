# System Architecture

This document describes the architectural design of the LinkedIn content automation pipeline. It outlines the layered separation of concerns and the component interactions.

## Architectural Layers

```
┌────────────────────────────────────────────────────────┐
│                    RESEARCH LAYER                      │
│ - fetch_reddit_apify.py                                │
│ - fetch_reddit_fallback.py                             │
│ - fetch_ai_news_rss.py                                 │
└───────────────────────────┬────────────────────────────┘
                            │ Raw JSON Feeds
                            ▼
┌────────────────────────────────────────────────────────┐
│                       AI LAYER                         │
│ - generate_all_content_gemini.py                       │
│ - correct_posts.py                                     │
└───────────────────────────┬────────────────────────────┘
                            │ Draft Texts & Config JSON
                            ▼
┌────────────────────────────────────────────────────────┐
│                ASSET GENERATION LAYER                  │
│ - generate_carousel_today.py                           │
│ - build_carousel_today.cjs                             │
│ - generate_infographic_today.py                        │
│ - cap_infographic_today.cjs                            │
└───────────────────────────┬────────────────────────────┘
                            │ Compiled PDFs & PNGs
                            ▼
┌────────────────────────────────────────────────────────┐
│                   PUBLISHING LAYER                     │
│ - send_to_slack.py                                     │
│ - schedule_all_posts.cjs                               │
└────────────────────────────────────────────────────────┘
```

---

### 1. Research Layer
* **Role**: Scrapes and aggregates trending source signals.
* **Core Components**:
  * [fetch_reddit_apify.py](file:///Users/anny/Downloads/Archives/instagram/fetch_reddit_apify.py) (Primary Reddit scraper using Apify API)
  * [fetch_reddit_fallback.py](file:///Users/anny/Downloads/Archives/instagram/fetch_reddit_fallback.py) (JSON endpoint scraping fallback)
  * [fetch_reddit_rss.py](file:///Users/anny/Downloads/Archives/instagram/fetch_reddit_rss.py) (RSS fallback)
  * [fetch_ai_news_rss.py](file:///Users/anny/Downloads/Archives/instagram/fetch_ai_news_rss.py) (AI newsletters RSS parser)

### 2. AI Layer
* **Role**: Integrates with LLMs to generate high-quality text drafts and structured design parameters.
* **Core Components**:
  * [generate_all_content_gemini.py](file:///Users/anny/Downloads/Archives/instagram/generate_all_content_gemini.py) (Generates text content and design configurations via OpenRouter)
  * [correct_posts.py](file:///Users/anny/Downloads/Archives/instagram/correct_posts.py) (Post-processing script to sanitize text drafts)

### 3. Prompt Layer
* **Role**: Contains the system prompts, voice patterns, and constraints.
* **Core Components**:
  * [commands/linkedin-content.md](file:///Users/anny/Downloads/Archives/instagram/commands/linkedin-content.md)
  * [skills/linkedin-ai-news-engine/SKILL.md](file:///Users/anny/Downloads/Archives/instagram/skills/linkedin-ai-news-engine/SKILL.md)
  * [skills/linkedin-performance-engine/SKILL.md](file:///Users/anny/Downloads/Archives/instagram/skills/linkedin-performance-engine/SKILL.md)

### 4. Visual Asset Generation Layer
* **Role**: Assembles dynamic slides and infographics in HTML, and compiles them to PDF/PNG formats using Puppeteer.
* **Core Components**:
  * [generate_carousel_today.py](file:///Users/anny/Downloads/Archives/instagram/generate_carousel_today.py) (Merges JSON data into HTML templates)
  * [build_carousel_today.cjs](file:///Users/anny/Downloads/Archives/instagram/build_carousel_today.cjs) (Compiles slide HTMLs into a multi-page PDF)
  * [generate_infographic_today.py](file:///Users/anny/Downloads/Archives/instagram/generate_infographic_today.py) (Merges stats into infographic template HTML)
  * [cap_infographic_today.cjs](file:///Users/anny/Downloads/Archives/instagram/cap_infographic_today.cjs) (Captures infographic HTML to PNG)

### 5. Publishing Layer
* **Role**: Transports draft materials and schedules them on LinkedIn.
* **Core Components**:
  * [send_to_slack.py](file:///Users/anny/Downloads/Archives/instagram/send_to_slack.py) (Posts texts and uploads graphics to Slack)
  * [schedule_all_posts.cjs](file:///Users/anny/Downloads/Archives/instagram/schedule_all_posts.cjs) (Performs browser-level LinkedIn scheduling automation)

### 6. Configuration Layer
* **Role**: Loads external secrets and runtime parameters.
* **Core Components**:
  * [.env](file:///Users/anny/Downloads/Archives/instagram/.env) (Loaded dynamically inside Python and Node.js environments)

### 7. Logging Layer
* **Role**: Keeps track of visual styles and topics used in recent runs.
* **Core Components**:
  * [carousel-hook-log.json](file:///Users/anny/Downloads/Archives/instagram/carousel-hook-log.json)
  * [infographic-run-log.json](file:///Users/anny/Downloads/Archives/instagram/infographic-run-log.json)
  * [performance-run-log.json](file:///Users/anny/Downloads/Archives/instagram/performance-run-log.json)
