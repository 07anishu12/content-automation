# Migration Summary Report

This report summarizes key steps required to migrate the LinkedIn automation pipeline to an Instagram automation platform.

---

## 1. Pipeline Reuse vs. Replacement Breakdown

* **Reused Components**: ~60% of the codebase can be repurposed:
  * Scrapers ([fetch_reddit_apify.py](file:///Users/anny/Downloads/Archives/instagram/fetch_reddit_apify.py), [fetch_ai_news_rss.py](file:///Users/anny/Downloads/Archives/instagram/fetch_ai_news_rss.py)).
  * Revision Engine ([correct_posts.py](file:///Users/anny/Downloads/Archives/instagram/correct_posts.py)).
  * Visual assets renderer ([build_carousel_today.cjs](file:///Users/anny/Downloads/Archives/instagram/build_carousel_today.cjs), [cap_infographic_today.cjs](file:///Users/anny/Downloads/Archives/instagram/cap_infographic_today.cjs)).
  * Slack Approvals ([send_to_slack.py](file:///Users/anny/Downloads/Archives/instagram/send_to_slack.py)).
* **Replaced Components**: ~40% of the codebase must be replaced or heavily modified:
  * LinkedIn UI Automator ([schedule_all_posts.cjs](file:///Users/anny/Downloads/Archives/instagram/schedule_all_posts.cjs)).
  * Formatting instructions ([commands/linkedin-content.md](file:///Users/anny/Downloads/Archives/instagram/commands/linkedin-content.md)).
  * Account performance heuristics ([skills/linkedin-performance-engine/SKILL.md](file:///Users/anny/Downloads/Archives/instagram/skills/linkedin-performance-engine/SKILL.md)).

---

## 2. Key Migration Requirements

### Visual Assets Adjustment
* **Instagram Grid Layout**: Instagram carousels require separate slide images (e.g. $1080 \times 1080\text{px}$ or $1080 \times 1350\text{px}$ portrait format) rather than a single merged PDF file.
* **Modification Plan**: Modify the carousel compiler script ([build_carousel_today.cjs](file:///Users/anny/Downloads/Archives/instagram/build_carousel_today.cjs)) to output a ZIP folder of the individual slide PNG images rather than compiling them into a single PDF.

### content-doctrine Reframing
* **Target Audience**: Transition from general tech/AI professionals to individuals looking for two-wheeler financing, motorcycle enthusiasts, and local vehicle dealers.
* **Topic Scope**: Reframe content around bike reviews, financing tips, EMI breakdowns, interest rate comparisons, and ownership economics.

### Publishing Engine Replacement
* **Instagram Publishing**: Swap the LinkedIn Puppeteer scheduling engine for Instagram Graph API calls (for business accounts) or mobile web browser simulation scripts using Puppeteer.
