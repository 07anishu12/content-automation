# Migration Readiness Assessment

This document classifies all core files in the repository to assess their readiness for a future migration to an Instagram automation platform.

---

## 1. Classification Definitions
* **Core Reusable**: Functional modules that can be moved to the new platform with minimal changes.
* **LinkedIn-specific**: Code containing selectors, workflows, or rules tied to LinkedIn. Requires replacement.
* **Utility**: Helper scripts performing tasks like format conversions.
* **Infrastructure**: Environment settings and scrapers.
* **Asset Generation**: Code that builds image or PDF attachments.
* **Publishing**: Transports compiled posts to their destinations.
* **Candidate for Refactoring**: Code containing hardcoded paths or tightly-coupled logic that should be cleaned up.
* **Candidate for Deletion**: Deprecated scripts or duplicates that can be safely removed.

---

## 2. File Classifications

| File Name | Classification | Migration Impact & Plan |
|---|---|---|
| **[fetch_reddit_apify.py](file:///Users/anny/Downloads/Archives/instagram/fetch_reddit_apify.py)** | Core Reusable / Infrastructure | **Keep**. Update target subreddits to focus on two-wheeler/automotive finance topics. |
| **[fetch_ai_news_rss.py](file:///Users/anny/Downloads/Archives/instagram/fetch_ai_news_rss.py)** | Core Reusable / Infrastructure | **Keep**. Update RSS urls to target automotive, banking, and fintech blogs. |
| **[generate_all_content_gemini.py](file:///Users/anny/Downloads/Archives/instagram/generate_all_content_gemini.py)** | Candidate for Refactoring | **Refactor**. Split post generation from visual asset configuration. Reframe prompts around two-wheeler financing. |
| **[correct_posts.py](file:///Users/anny/Downloads/Archives/instagram/correct_posts.py)** | Candidate for Refactoring | **Refactor**. Update target brand references from "FounderWing" to the new two-wheeler finance brand. |
| **[generate_carousel_today.py](file:///Users/anny/Downloads/Archives/instagram/generate_carousel_today.py)** | Asset Generation | **Modify**. Switch templates to fit Instagram's visual guidelines. Adjust hardcoded skill paths. |
| **[build_carousel_today.cjs](file:///Users/anny/Downloads/Archives/instagram/build_carousel_today.cjs)** | Asset Generation / Publishing | **Modify**. Change PDF export logic to export a ZIP archive of individual slide PNGs (Instagram carousels require separate images). |
| **[generate_infographic_today.py](file:///Users/anny/Downloads/Archives/instagram/generate_infographic_today.py)** | Asset Generation | **Keep**. Update infographic template styling to match the new brand identity. |
| **[cap_infographic_today.cjs](file:///Users/anny/Downloads/Archives/instagram/cap_infographic_today.cjs)** | Asset Generation | **Keep**. Renders square images, which fits Instagram's grid format. |
| **[send_to_slack.py](file:///Users/anny/Downloads/Archives/instagram/send_to_slack.py)** | Core Reusable / Publishing | **Keep**. Reusable for team preview approvals. |
| **[schedule_all_posts.cjs](file:///Users/anny/Downloads/Archives/instagram/schedule_all_posts.cjs)** | LinkedIn-specific / Publishing | **Replace**. Swap with browser automation or API integration targeting Instagram. |
| **[delete_all_scheduled.cjs](file:///Users/anny/Downloads/Archives/instagram/delete_all_scheduled.cjs)** | LinkedIn-specific / Publishing | **Replace / Delete**. |
| **[inspect_scheduled_posts.cjs](file:///Users/anny/Downloads/Archives/instagram/inspect_scheduled_posts.cjs)** | LinkedIn-specific / Utility | **Replace / Delete**. |
| **[convert_base64.py](file:///Users/anny/Downloads/Archives/instagram/convert_base64.py)** | Utility | **Keep**. |
| **[convert_carousel_base64.py](file:///Users/anny/Downloads/Archives/instagram/convert_carousel_base64.py)** | Utility | **Keep**. |
| **[convert_pdf_base64.py](file:///Users/anny/Downloads/Archives/instagram/convert_pdf_base64.py)** | Utility | **Keep**. |
| **[aigen_image.py](file:///Users/anny/Downloads/Archives/instagram/aigen_image.py)** | Utility | **Keep**. |
| **[change_time.py](file:///Users/anny/Downloads/Archives/instagram/change_time.py)** | Utility | **Keep**. |
| **[press_tabs.py](file:///Users/anny/Downloads/Archives/instagram/press_tabs.py)** | Candidate for Deletion | **Delete**. Simple key emulator with no integration context. |
| **[fetch_reddit_puppeteer.js](file:///Users/anny/Downloads/Archives/instagram/fetch_reddit_puppeteer.js)** | Candidate for Deletion | **Delete**. Replaced by Apify scraper. |
