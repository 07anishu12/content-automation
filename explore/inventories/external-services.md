# External Services Inventory

This document outlines the third-party platforms and API services used by the system.

---

## 1. OpenRouter
* **Purpose**: Accesses language models (such as `google/gemma-4-31b-it:free`) to generate text content.
* **Credentials**: Bearer token query auth (`OPENROUTER_API_KEY`).
* **Endpoint**: `https://openrouter.ai/api/v1/chat/completions`.

---

## 2. Apify
* **Purpose**: Runs actor scraping profiles (`trudax/reddit-scraper-lite`) to gather trending posts from Reddit.
* **Credentials**: Bearer token query parameter (`APIFY_API_KEY`).
* **Endpoint**: `https://api.apify.com/v2/`.

---

## 3. Slack
* **Purpose**: Delivers post drafts and visual files to the team reviews channel.
* **Credentials**: Bearer token auth (`SLACK_BOT_TOKEN`).
* **Endpoints**:
  * `https://slack.com/api/files.getUploadURLExternal`
  * `https://slack.com/api/files.completeUploadExternal`
  * `https://slack.com/api/chat.postMessage`

---

## 4. Unsplash
* **Purpose**: Serves as a fallback image source if local visual assets are missing or corrupted.
* **Authentication**: None.
* **Endpoint**: `https://images.unsplash.com/`.
