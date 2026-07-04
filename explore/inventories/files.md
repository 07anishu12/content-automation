# Core Files Inventory

This document lists the files in the codebase, detailing their runtime execution type.

---

## 1. Orchestration & Content Generators

* **[generate_all_content_gemini.py](file:///Users/anny/Downloads/Archives/instagram/generate_all_content_gemini.py)**: Python. Calls OpenRouter to generate 11 posts, carousel slide JSON configs, and infographic data configs.
* **[correct_posts.py](file:///Users/anny/Downloads/Archives/instagram/correct_posts.py)**: Python. revision pass to clean draft texts.
* **[generate_posts_via_openrouter.py](file:///Users/anny/Downloads/Archives/instagram/generate_posts_via_openrouter.py)**: Python. Alternative script targeting OpenRouter.
* **[generate_posts_via_anthropic.py](file:///Users/anny/Downloads/Archives/instagram/generate_posts_via_anthropic.py)**: Python. Alternative script targeting Claude.

---

## 2. Scraping & Data Fetching

* **[fetch_reddit_apify.py](file:///Users/anny/Downloads/Archives/instagram/fetch_reddit_apify.py)**: Python. Scrapes trending subreddits using the Apify API.
* **[fetch_reddit_fallback.py](file:///Users/anny/Downloads/Archives/instagram/fetch_reddit_fallback.py)**: Python. Directly parses Reddit JSON feeds.
* **[fetch_reddit_rss.py](file:///Users/anny/Downloads/Archives/instagram/fetch_reddit_rss.py)**: Python. Fallback parser using RSS feed templates.
* **[fetch_ai_news_rss.py](file:///Users/anny/Downloads/Archives/instagram/fetch_ai_news_rss.py)**: Python. Scrapes news feeds from TechCrunch and VentureBeat.

---

## 3. Visual Rendering & Compiling

* **[generate_carousel_today.py](file:///Users/anny/Downloads/Archives/instagram/generate_carousel_today.py)**: Python. Generates static HTML slide templates.
* **[build_carousel_today.cjs](file:///Users/anny/Downloads/Archives/instagram/build_carousel_today.cjs)**: JavaScript (CommonJS). Renders HTML slides to PNGs and compiles a multi-page PDF.
* **[generate_infographic_today.py](file:///Users/anny/Downloads/Archives/instagram/generate_infographic_today.py)**: Python. Merges stats into infographic HTML templates.
* **[cap_infographic_today.cjs](file:///Users/anny/Downloads/Archives/instagram/cap_infographic_today.cjs)**: JavaScript. Screenshots the infographic HTML to a PNG file.

---

## 4. Scheduling & Publishing

* **[schedule_all_posts.cjs](file:///Users/anny/Downloads/Archives/instagram/schedule_all_posts.cjs)**: JavaScript. Automates scheduling on LinkedIn via Puppeteer.
* **[send_to_slack.py](file:///Users/anny/Downloads/Archives/instagram/send_to_slack.py)**: Python. Uploads final text and visual assets to Slack.
