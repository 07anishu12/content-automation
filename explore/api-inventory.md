# API Inventory

This document details the external APIs used by the content automation pipeline.

---

## 1. OpenRouter API
* **Role**: Primary endpoint for content drafting and post revisions.
* **Endpoint**: `POST https://openrouter.ai/api/v1/chat/completions`
* **Authentication**: Bearer Token (`OPENROUTER_API_KEY` environment variable).
* **Used in**:
  * [generate_all_content_gemini.py](file:///Users/anny/Downloads/Archives/instagram/generate_all_content_gemini.py#L27)
  * [correct_posts.py](file:///Users/anny/Downloads/Archives/instagram/correct_posts.py#L50)
* **Retry Logic**: Retries up to 5 times. If it receives a `429` (Rate Limit) status code, it sleeps for `10 * (attempt + 1)` seconds before retrying.
* **Response Format**: Standard completions choices format containing messages text.

---

## 2. Apify Actor API
* **Role**: Scrapes trending posts from Reddit.
* **Endpoints**:
  * **Trigger Run**: `POST https://api.apify.com/v2/acts/trudax~reddit-scraper-lite/runs?token={token}`
  * **Check Status**: `GET https://api.apify.com/v2/actor-runs/{run_id}?token={token}`
  * **Get Dataset Items**: `GET https://api.apify.com/v2/datasets/{dataset_id}/items?token={token}&limit=100`
* **Authentication**: Token Query Parameter (`APIFY_API_KEY` environment variable).
* **Used in**:
  * [fetch_reddit_apify.py](file:///Users/anny/Downloads/Archives/instagram/fetch_reddit_apify.py#L37)
* **Error Handling**: Polling loop checks status and exits if the job fails, times out, or is aborted.

---

## 3. Slack Web API
* **Role**: Uploads media files and sends text messages to the team reviews channel.
* **Endpoints**:
  * **Initiate Upload**: `POST https://slack.com/api/files.getUploadURLExternal`
  * **Upload Bytes**: `POST {upload_url}` (returned from Slack)
  * **Complete Upload**: `POST https://slack.com/api/files.completeUploadExternal`
  * **Post Message**: `POST https://slack.com/api/chat.postMessage`
* **Authentication**: Bearer Token (`SLACK_BOT_TOKEN` environment variable).
* **Used in**:
  * [send_to_slack.py](file:///Users/anny/Downloads/Archives/instagram/send_to_slack.py#L25)
* **Error Handling**: Checks the returned JSON response's `ok` boolean flag and logs errors if `ok` is `false`.
