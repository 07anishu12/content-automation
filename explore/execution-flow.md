# Execution Flow

This document details the step-by-step runtime execution of the automated pipeline.

## Main Execution Cycle

```
Start
  ↓
1. Data Fetching
   - Run fetch_reddit_apify.py (or fallback files)
   - Run fetch_ai_news_rss.py
  ↓
2. Bootstrap & Deduplication Checking
   - Read content-doctrine.md, carousel-hook-log.json, infographic-run-log.json, performance-run-log.json
  ↓
3. AI Generation
   - Execute generate_all_content_gemini.py
   - Calls OpenRouter for 11 posts, carousel_data.json, infographic_data.json, and 5 performance posts
  ↓
4. Text Sanitization
   - Run correct_posts.py to purge corporate buzzwords and add Brand mentions
  ↓
5. Visual Asset Compilation
   - Run generate_carousel_today.py and build_carousel_today.cjs (generate HTML -> Puppeteer screenshot -> PDF merge)
   - Run generate_infographic_today.py and cap_infographic_today.cjs (generate HTML -> PNG screenshot)
  ↓
6. Slack Verification
   - Run send_to_slack.py to upload text drafts and assets
  ↓
7. Social Scheduling
   - Run schedule_all_posts.cjs using Puppeteer to fill and schedule in LinkedIn UI
  ↓
8. Log Update
   - Update carousel-hook-log.json, infographic-run-log.json, performance-run-log.json
  ↓
Finish
```

---

## Detailed Step Explanations

### Step 1: Data Fetching
* **Target Files**:
  * [fetch_reddit_apify.py](file:///Users/anny/Downloads/Archives/instagram/fetch_reddit_apify.py)
  * [fetch_ai_news_rss.py](file:///Users/anny/Downloads/Archives/instagram/fetch_ai_news_rss.py)
* **Description**: The system starts by fetching raw posts from specific subreddits (using Apify Scraper Lite) and AI RSS feeds. The output files [reddit_data.json](file:///Users/anny/Downloads/Archives/instagram/reddit_data.json) and [ai_news_data.json](file:///Users/anny/Downloads/Archives/instagram/ai_news_data.json) are stored in the root.

### Step 2: Bootstrap & Deduplication
* **Target Files**:
  * [carousel-hook-log.json](file:///Users/anny/Downloads/Archives/instagram/carousel-hook-log.json)
  * [infographic-run-log.json](file:///Users/anny/Downloads/Archives/instagram/infographic-run-log.json)
  * [performance-run-log.json](file:///Users/anny/Downloads/Archives/instagram/performance-run-log.json)
* **Description**: Dynamic configuration checks are performed to ensure recently used hook styles, infographic topics, and performance categories are banned from the upcoming generation.

### Step 3: AI Generation
* **Target Files**:
  * [generate_all_content_gemini.py](file:///Users/anny/Downloads/Archives/instagram/generate_all_content_gemini.py)
* **Description**: Connects to OpenRouter using `google/gemma-4-31b-it:free` to generate a draft of all posts and structural configurations for visuals.

### Step 4: Text Sanitization
* **Target Files**:
  * [correct_posts.py](file:///Users/anny/Downloads/Archives/instagram/correct_posts.py)
* **Description**: An automated revision pass scans the text drafts and prompts the LLM to remove any banned words (e.g., *delve*, *leverage*) and insert mandatory brand references ("FounderWing").

### Step 5: Visual Asset Compilation
* **Target Files**:
  * [generate_carousel_today.py](file:///Users/anny/Downloads/Archives/instagram/generate_carousel_today.py)
  * [build_carousel_today.cjs](file:///Users/anny/Downloads/Archives/instagram/build_carousel_today.cjs)
  * [generate_infographic_today.py](file:///Users/anny/Downloads/Archives/instagram/generate_infographic_today.py)
  * [cap_infographic_today.cjs](file:///Users/anny/Downloads/Archives/instagram/cap_infographic_today.cjs)
* **Description**: Renders HTML files, opens them in a headless browser, screenshots them, and merges them into a PDF carousel.

### Step 6: Slack Verification
* **Target Files**:
  * [send_to_slack.py](file:///Users/anny/Downloads/Archives/instagram/send_to_slack.py)
* **Description**: Transports texts, carousel PDFs, and infographic PNGs to the Slack workspace for manual preview.

### Step 7: Social Scheduling
* **Target Files**:
  * [schedule_all_posts.cjs](file:///Users/anny/Downloads/Archives/instagram/schedule_all_posts.cjs)
* **Description**: Logs in to LinkedIn, triggers the posting modal, types post texts, attaches media files, sets the dates, and completes scheduling.

### Step 8: Log Update
* **Description**: Updates the local JSON files to register today's run parameters, ensuring the next run's deduplication check behaves correctly.
