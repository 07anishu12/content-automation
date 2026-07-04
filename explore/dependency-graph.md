# File Dependencies and Imports

This document describes the dependency relationships, imports, inputs, and outputs for the core files in the project.

## Dependency Graph Overview

```
[ fetch_reddit_apify.py ] ──────┐
                                │
[ fetch_ai_news_rss.py ]  ──────┼─► [ reddit_data.json ]
                                │   [ ai_news_data.json ]
                                │          │
                                │          ▼
                                └─► [ generate_all_content_gemini.py ]
                                           │
                                           ├─► [ linkedin_posts_today.txt ] ──► [ correct_posts.py ] ──► [ clean_posts ]
                                           ├─► [ carousel_data.json ] ──► [ generate_carousel_today.py ] ──► [ build_carousel_today.cjs ]
                                           └─► [ infographic_data.json ] ──► [ generate_infographic_today.py ] ──► [ cap_infographic_today.cjs ]
```

---

## File Details

### 1. [fetch_reddit_apify.py](file:///Users/anny/Downloads/Archives/instagram/fetch_reddit_apify.py)
* **Description**: Primary Reddit scraper.
* **Imports**: `os`, `json`, `urllib.request`, `urllib.parse`, `time`, `ssl`.
* **APIs**: Apify Runs API.
* **Inputs**: `APIFY_API_KEY` (from environment).
* **Outputs**: Writes [reddit_data.json](file:///Users/anny/Downloads/Archives/instagram/reddit_data.json).

### 2. [fetch_ai_news_rss.py](file:///Users/anny/Downloads/Archives/instagram/fetch_ai_news_rss.py)
* **Description**: Scrapes newsletter articles.
* **Imports**: `urllib.request`, `xml.etree.ElementTree`, `json`, `ssl`, `re`, `html`.
* **APIs**: Technical blogs RSS feeds.
* **Inputs**: Configured RSS feed URL strings.
* **Outputs**: Writes [ai_news_data.json](file:///Users/anny/Downloads/Archives/instagram/ai_news_data.json).

### 3. [generate_all_content_gemini.py](file:///Users/anny/Downloads/Archives/instagram/generate_all_content_gemini.py)
* **Description**: Main content generator.
* **Imports**: `json`, `urllib.request`, `ssl`, `sys`, `os`, `datetime`, `time`, `traceback`.
* **APIs**: OpenRouter Completions API.
* **Inputs**: [reddit_data.json](file:///Users/anny/Downloads/Archives/instagram/reddit_data.json), [ai_news_data.json](file:///Users/anny/Downloads/Archives/instagram/ai_news_data.json), and `.env` credentials.
* **Outputs**:
  * [linkedin_posts_today.txt](file:///Users/anny/Downloads/Archives/instagram/linkedin_posts_today.txt) (Raw posts)
  * [carousel_data.json](file:///Users/anny/Downloads/Archives/instagram/carousel_data.json) (Carousel structure)
  * [infographic_data.json](file:///Users/anny/Downloads/Archives/instagram/infographic_data.json) (Infographic stats)
  * `performance_posts_YYYYMMDD.txt`

### 4. [correct_posts.py](file:///Users/anny/Downloads/Archives/instagram/correct_posts.py)
* **Description**: Sanitizes text drafts.
* **Imports**: `os`, `json`, `urllib.request`, `urllib.parse`, `ssl`, `datetime`, `time`.
* **APIs**: OpenRouter Completions API.
* **Inputs**: Reads [linkedin_posts_today.txt](file:///Users/anny/Downloads/Archives/instagram/linkedin_posts_today.txt).
* **Outputs**: Overwrites [linkedin_posts_today.txt](file:///Users/anny/Downloads/Archives/instagram/linkedin_posts_today.txt) with cleaned text.

### 5. [generate_carousel_today.py](file:///Users/anny/Downloads/Archives/instagram/generate_carousel_today.py)
* **Description**: Translates carousel JSON data into slide HTML templates.
* **Imports**: `os`, `re`, `urllib.request`, `ssl`, `json`.
* **Inputs**: [carousel_data.json](file:///Users/anny/Downloads/Archives/instagram/carousel_data.json) and template string mappings.
* **Outputs**: Generates files under `temp/carousel-branded/slide-0[1-7].html`.

### 6. [build_carousel_today.cjs](file:///Users/anny/Downloads/Archives/instagram/build_carousel_today.cjs)
* **Description**: Orchestrates slide rendering.
* **Requires**: `puppeteer-core`, `fs`, `path`, `child_process`.
* **Inputs**: Reads slide HTMLs from `temp/`.
* **Outputs**: Exports slide PNGs and compiles `linkedin-carousel-YYYY-MM-DD.pdf` under `output/`.

### 7. [generate_infographic_today.py](file:///Users/anny/Downloads/Archives/instagram/generate_infographic_today.py)
* **Description**: Merges stat JSON data into the infographic base HTML template.
* **Imports**: `json`, `os`, `re`.
* **Inputs**: [infographic_data.json](file:///Users/anny/Downloads/Archives/instagram/infographic_data.json) and [linkedin-infographic-template.html](file:///Users/anny/Downloads/Archives/instagram/linkedin-infographic-template.html).
* **Outputs**: Writes [linkedin-infographic.html](file:///Users/anny/Downloads/Archives/instagram/linkedin-infographic.html).

### 8. [cap_infographic_today.cjs](file:///Users/anny/Downloads/Archives/instagram/cap_infographic_today.cjs)
* **Description**: Opens infographic HTML in Puppeteer and screenshots it to a square PNG.
* **Requires**: `puppeteer-core`, `fs`, `path`.
* **Inputs**: [linkedin-infographic.html](file:///Users/anny/Downloads/Archives/instagram/linkedin-infographic.html).
* **Outputs**: Saves `linkedin-infographic-YYYYMMDD.png` to `slack_downloads/`.

### 9. [send_to_slack.py](file:///Users/anny/Downloads/Archives/instagram/send_to_slack.py)
* **Description**: Delivers compiled texts and media attachments to Slack.
* **Imports**: `os`, `json`, `urllib.request`, `urllib.parse`, `datetime`.
* **APIs**: Slack Web API.
* **Inputs**: Reads texts from files and media files from the workspace.
* **Outputs**: Terminal status logs.

### 10. [schedule_all_posts.cjs](file:///Users/anny/Downloads/Archives/instagram/schedule_all_posts.cjs)
* **Description**: Automatically inputs and schedules the compiled content batch on LinkedIn.
* **Requires**: `puppeteer-core`, `fs`, `path`, `os`.
* **APIs**: Headless Chromium instance connecting to LinkedIn.
* **Inputs**: Read post texts and PDF/PNG attachments from `slack_downloads/`.
* **Outputs**: Browser confirmation logs of completed schedules.
