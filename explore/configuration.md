# Configuration Audit

This document lists all environment variables, constants, config files, and default values used across the pipeline.

---

## 1. Environment Variables ([.env](file:///Users/anny/Downloads/Archives/instagram/.env))

| Variable Name | Purpose | Where Used | Secret? |
|---|---|---|---|
| **`APIFY_API_KEY`** | Authenticates Apify API calls | `fetch_reddit_apify.py` | Yes |
| **`OPENROUTER_API_KEY`** | Authenticates OpenRouter API calls | `generate_all_content_gemini.py`<br>`correct_posts.py` | Yes |
| **`SLACK_BOT_TOKEN`** | Authenticates Slack API file uploads and messages | `send_to_slack.py` | Yes |
| **`SCRAPINGDOG_API_KEY`**| Optional scraper key | Not actively used in core | Yes |
| **`ANTHROPIC_API_KEY`**  | Direct alternative for Claude API | `generate_posts_via_anthropic.py` | Yes |
| **`GEMINI_API_KEY`**     | Direct alternative for Google Gemini API | `generate_daily_paper.py` | Yes |

---

## 2. Hardcoded Constants & Settings

### Node.js Render Configs
* **Canvas Dimension**: $1080 \times 1080\text{px}$ (Device scale factor: `2` for high-DPI retina display screenshots).
  * Used in: [build_carousel_today.cjs](file:///Users/anny/Downloads/Archives/instagram/build_carousel_today.cjs#L31) and [cap_infographic_today.cjs](file:///Users/anny/Downloads/Archives/instagram/cap_infographic_today.cjs#L31).
* **Mac Chrome Application Path**: `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`.
  * Used in Puppeteer launch scripts: [build_carousel_today.cjs](file:///Users/anny/Downloads/Archives/instagram/build_carousel_today.cjs#L16).
* **Keychain Arguments**: `--use-mock-keychain`, `--password-store=basic`.
  * Used to bypass macOS system security authorization checks during automated headless browser startup.

### Slack Configurations
* **Review Channel ID**: `C0AVBBTD529`.
  * Target channel for reviews in [send_to_slack.py](file:///Users/anny/Downloads/Archives/instagram/send_to_slack.py#L19).

### LLM Completions Settings
* **OpenRouter Model**: `google/gemma-4-31b-it:free`.
* **Max Tokens**: `4000`.
* **OpenRouter URL**: `https://openrouter.ai/api/v1/chat/completions`.
