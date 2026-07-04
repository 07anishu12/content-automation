# Environment Reference Sheet

Here is the reference sheet showing where each configuration variable is loaded and validated:

| Config Variable | Loaded By File | Line Reference | Fallback Default |
|---|---|---|---|
| **`APIFY_API_KEY`** | `fetch_reddit_apify.py` | [Line 16](file:///Users/anny/Downloads/Archives/instagram/fetch_reddit_apify.py#L16) | Exits if missing |
| **`OPENROUTER_API_KEY`** | `generate_all_content_gemini.py` | [Line 18](file:///Users/anny/Downloads/Archives/instagram/generate_all_content_gemini.py#L18) | Exits if missing |
| **`OPENROUTER_API_KEY`** | `correct_posts.py` | [Line 18](file:///Users/anny/Downloads/Archives/instagram/correct_posts.py#L18) | Exits if missing |
| **`SLACK_BOT_TOKEN`** | `send_to_slack.py` | [Line 11](file:///Users/anny/Downloads/Archives/instagram/send_to_slack.py#L11) | Exits if missing |
| **`ANTHROPIC_API_KEY`** | `generate_posts_via_anthropic.py` | [Line 18](file:///Users/anny/Downloads/Archives/instagram/generate_posts_via_anthropic.py#L18) | Exits if missing |
| **`GEMINI_API_KEY`** | `generate_daily_paper.py` | [Line 19](file:///Users/anny/Downloads/Archives/instagram/generate_daily_paper.py#L19) | Exits if missing |

### Script Settings
* **Urllib SSL context override**: In Python script files (e.g. [fetch_reddit_apify.py:L8](file:///Users/anny/Downloads/Archives/instagram/fetch_reddit_apify.py#L8)), the code configures context to bypass certification verification:
  ```python
  ctx = ssl.create_default_context()
  ctx.check_hostname = False
  ctx.verify_mode = ssl.CERT_NONE
  ```
  *This is done to avoid SSL handshake verification exceptions on local testing environments.*
