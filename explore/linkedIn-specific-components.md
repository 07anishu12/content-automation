# LinkedIn-Specific Components

This document catalogs the components that are tied to the LinkedIn platform and cannot be reused directly for other destinations.

---

## 1. Puppeteer Publishing Automation Scripts
These scripts contain selector configurations and step sequences designed for LinkedIn's web UI. They are highly fragile and will break if LinkedIn updates its markup:
* **[schedule_all_posts.cjs](file:///Users/anny/Downloads/Archives/instagram/schedule_all_posts.cjs)**: Navigates the posting and scheduling workflow on the LinkedIn desktop interface.
* **[schedule_four_posts.cjs](file:///Users/anny/Downloads/Archives/instagram/schedule_four_posts.cjs)**: Schedules only the 4 Reddit-based posts.
* **[schedule_other_posts.cjs](file:///Users/anny/Downloads/Archives/instagram/schedule_other_posts.cjs)**: Schedules remaining posts.
* **[delete_all_scheduled.cjs](file:///Users/anny/Downloads/Archives/instagram/delete_all_scheduled.cjs)**: Automates post deletion inside the scheduled posts modal.
* **[edit_scheduled_posts.cjs](file:///Users/anny/Downloads/Archives/instagram/edit_scheduled_posts.cjs)**: Edits scheduling times or texts.
* **[inspect_scheduled_posts.cjs](file:///Users/anny/Downloads/Archives/instagram/inspect_scheduled_posts.cjs)**: Inspects active scheduled items.
* **[verify_scheduled_posts.cjs](file:///Users/anny/Downloads/Archives/instagram/verify_scheduled_posts.cjs)**: Compares scheduled items on screen against local logs to verify success.

---

## 2. Text Style Guides & Formatting Rules
* **[commands/linkedin-content.md](file:///Users/anny/Downloads/Archives/instagram/commands/linkedin-content.md)**: Defines specific rules for LinkedIn formatting (e.g. 6-part structure, CTA copy templates, and post length limits).

---

## 3. Analytics Performance Engine
* **[skills/linkedin-performance-engine/SKILL.md](file:///Users/anny/Downloads/Archives/instagram/skills/linkedin-performance-engine/SKILL.md)**: Leverages historical analytical patterns specific to the `@founderswing` LinkedIn page.
* **[founderswing_linkedin_content_report.md](file:///Users/anny/Downloads/Archives/instagram/founderswing_linkedin_content_report.md)**: Raw text report of previous LinkedIn post performances.
