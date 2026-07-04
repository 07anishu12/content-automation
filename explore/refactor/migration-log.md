# Migration Log

This document catalogs the step-by-step updates performed to decoupled and isolate LinkedIn files during the refactoring process.

---

* **Step 1**: Created base directory layouts (`core/`, `adapters/`, `shared/`, `tests/`).
* **Step 2**: Extracted configuration settings into `core/config/config.py` and `core/config/config.cjs`.
* **Step 3**: Created Python domain dataclasses inside `core/models/models.py`.
* **Step 4**: Created abstract system operations under `core/interfaces/interfaces.py`.
* **Step 5**: Built core services (`llm_service.py`, `file_service.py`) and helper utilities (`json_helper.py`, `date_helper.py`).
* **Step 6**: Replicated LinkedIn-specific files inside the `adapters/linkedin/` directory structure.
* **Step 7**: Updated imports in `generate_all_content_gemini.py`, `correct_posts.py`, `send_to_slack.py`, `fetch_reddit_apify.py`, and `build_carousel_today.cjs` to reference new central configuration and core services.
* **Step 8**: Appended updates to [explore/documentation.md](file:///Users/anny/Downloads/Archives/instagram/explore/documentation.md).
