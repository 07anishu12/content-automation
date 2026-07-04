# Reusable System Components

This document identifies components that are platform-independent and can be reused in future social media automation integrations (such as Instagram or X/Twitter).

---

## 1. Data Fetching Modules
These scripts fetch trending topics and news articles, and write raw JSON output files without relying on any social media publishing APIs:
* **[fetch_reddit_apify.py](file:///Users/anny/Downloads/Archives/instagram/fetch_reddit_apify.py)**: Scrapes subreddit posts. It only needs the subreddits list adjusted for new target niches.
* **[fetch_reddit_fallback.py](file:///Users/anny/Downloads/Archives/instagram/fetch_reddit_fallback.py)**: Directly fetches JSON endpoints without requiring API credentials.
* **[fetch_ai_news_rss.py](file:///Users/anny/Downloads/Archives/instagram/fetch_ai_news_rss.py)**: Parses standard XML RSS feeds.

---

## 2. Text Sanitization Engine
The word cleanup and validation workflow is highly reusable:
* **[correct_posts.py](file:///Users/anny/Downloads/Archives/instagram/correct_posts.py)**: Can be updated with new rules, platform-specific handle insertion prompts, or platform-specific banned word lists.

---

## 3. Visual Asset Compiler
The HTML-to-image/PDF compilation system is decoupled from publishing platforms:
* **[generate_carousel_today.py](file:///Users/anny/Downloads/Archives/instagram/generate_carousel_today.py)**: Merges text values into HTML layouts.
* **[build_carousel_today.cjs](file:///Users/anny/Downloads/Archives/instagram/build_carousel_today.cjs)**: Launches headless Chrome, takes screenshots, and compiles a PDF.
* **[generate_infographic_today.py](file:///Users/anny/Downloads/Archives/instagram/generate_infographic_today.py)**: Fills HTML infographic layouts with stats.
* **[cap_infographic_today.cjs](file:///Users/anny/Downloads/Archives/instagram/cap_infographic_today.cjs)**: Screenshots HTML pages to square PNG images.

---

## 4. Slack Review Integration
* **[send_to_slack.py](file:///Users/anny/Downloads/Archives/instagram/send_to_slack.py)**: Handles file uploads and text messaging. This component is highly reusable for review workflows across any automated publishing system.

---

## 5. De-duplication Logs
* The file-based JSON logging mechanism ([carousel-hook-log.json](file:///Users/anny/Downloads/Archives/instagram/carousel-hook-log.json), [infographic-run-log.json](file:///Users/anny/Downloads/Archives/instagram/infographic-run-log.json)) is generic and can be adapted to track history for other social platforms.
