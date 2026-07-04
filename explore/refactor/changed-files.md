# Changed Files Catalog

This document catalogues every file that was changed during the core refactoring process.

---

## 1. Modified Production Files

* **[generate_all_content_gemini.py](file:///Users/anny/Downloads/Archives/instagram/generate_all_content_gemini.py)**:
  * *Why*: Manual `.env` reading and HTTP connections were decoupled.
  * *What changed*: Replaced manual connection lines and JSON cleanups with config and service imports.
* **[correct_posts.py](file:///Users/anny/Downloads/Archives/instagram/correct_posts.py)**:
  * *Why*: decopled manually built completions request loops.
  * *What changed*: Utilizes the new centralized `LLMService` wrapper.
* **[send_to_slack.py](file:///Users/anny/Downloads/Archives/instagram/send_to_slack.py)**:
  * *Why*: Replaced manual `.env` file parsing for `SLACK_BOT_TOKEN`.
  * *What changed*: Imports token and channel directly from the config module.
* **[fetch_reddit_apify.py](file:///Users/anny/Downloads/Archives/instagram/fetch_reddit_apify.py)**:
  * *Why*: Replaced manual `.env` file parsing for `APIFY_API_KEY`.
  * *What changed*: Imports token directly from config.
* **[build_carousel_today.cjs](file:///Users/anny/Downloads/Archives/instagram/build_carousel_today.cjs)**:
  * *Why*: Replaced hardcoded Chromium configurations and viewport options.
  * *What changed*: Imports configs from JS central package.

---

## 2. Newly Created Architectural Files

* **[core/config/config.py](file:///Users/anny/Downloads/Archives/instagram/core/config/config.py)**:Centralizes all Python environment settings.
* **[core/config/config.cjs](file:///Users/anny/Downloads/Archives/instagram/core/config/config.cjs)**: Centralizes all JavaScript configuration settings.
* **[core/models/models.py](file:///Users/anny/Downloads/Archives/instagram/core/models/models.py)**: Defines common Python dataclasses for pipeline types.
* **[core/services/llm_service.py](file:///Users/anny/Downloads/Archives/instagram/core/services/llm_service.py)**: Decouples LLM OpenRouter queries and retry logic.
* **[core/services/file_service.py](file:///Users/anny/Downloads/Archives/instagram/core/services/file_service.py)**: Abstracts local disk read/write actions.
* **[core/utils/json_helper.py](file:///Users/anny/Downloads/Archives/instagram/core/utils/json_helper.py)**: Cleans and parses LLM-generated JSON strings.
* **[core/utils/date_helper.py](file:///Users/anny/Downloads/Archives/instagram/core/utils/date_helper.py)**: Standardizes date retrieval functions.
* **[core/interfaces/interfaces.py](file:///Users/anny/Downloads/Archives/instagram/core/interfaces/interfaces.py)**: Standardizes system operations via Abstract Base Classes.
