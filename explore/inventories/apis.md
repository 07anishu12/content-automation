# System API Reference Sheets

Here is the quick reference sheet mapping APIs to the files that call them:

| External Service | Method | Endpoint URL | Authentication Type | Target Files |
|---|---|---|---|---|
| **OpenRouter** | `POST` | `/api/v1/chat/completions` | Bearer Token | `generate_all_content_gemini.py`<br>`correct_posts.py` |
| **Apify** | `POST` | `/v2/acts/trudax~reddit-scraper-lite/runs` | Query Token | `fetch_reddit_apify.py` |
| **Apify** | `GET` | `/v2/actor-runs/{run_id}` | Query Token | `fetch_reddit_apify.py` |
| **Apify** | `GET` | `/v2/datasets/{dataset_id}/items` | Query Token | `fetch_reddit_apify.py` |
| **Slack** | `POST` | `/api/files.getUploadURLExternal` | Bearer Token | `send_to_slack.py` |
| **Slack** | `POST` | `/api/files.completeUploadExternal` | Bearer Token | `send_to_slack.py` |
| **Slack** | `POST` | `/api/chat.postMessage` | Bearer Token | `send_to_slack.py`<br>`send_slack_message.py` |
| **Unsplash** | `GET` | `/photo-1460925895917...` | None | `generate_carousel_today.py` |
