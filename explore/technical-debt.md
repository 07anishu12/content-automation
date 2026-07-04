# Technical Debt Assessment

This document catalogs code smells, tight coupling, and design limitations found in the current codebase.

---

## 1. Tight Coupling & Hardcoded References

### Hardcoded User Paths
* **Issue**: Multiple scripts reference hardcoded local absolute file paths for user `/Users/prithal/` (e.g. [generate_carousel_today.py:L53](file:///Users/anny/Downloads/Archives/instagram/generate_carousel_today.py#L53), [schedule_four_posts.cjs:L187](file:///Users/anny/Downloads/Archives/instagram/schedule_four_posts.cjs#L187), and [cap_infographic.cjs:L10](file:///Users/anny/Downloads/Archives/instagram/carousel-routine/cap_infographic.cjs#L10)).
* **Impact**: The application fails to run on other environments without manual path edits.
* **Fix**: Use relative paths (`./`) or dynamic directory references (like `__dirname` in Node.js or `os.path.dirname(__file__)` in Python).

---

## 2. Code Duplication

### Scraping Logic
* **Issue**: Scraper scripts ([fetch_reddit_apify.py](file:///Users/anny/Downloads/Archives/instagram/fetch_reddit_apify.py), [fetch_reddit_fallback.py](file:///Users/anny/Downloads/Archives/instagram/fetch_reddit_fallback.py), and [fetch_reddit_rss.py](file:///Users/anny/Downloads/Archives/instagram/fetch_reddit_rss.py)) redefine similar subreddit target lists and payload extraction parameters.
* **Impact**: Adding or removing subreddits requires updating multiple files.
* **Fix**: Define target lists in a central configuration module and import them.

### visual capture scripts
* **Issue**: The codebase contains duplicate Puppeteer screenshotting scripts (e.g. `cap_infographic.js`, `cap_infographic.cjs`, `cap_infographic_today.js`, and `cap_infographic_today.cjs`).
* **Impact**: Code drift. Edits to one capture script won't carry over to the others.
* **Fix**: Consolidate screenshot logic into a single module.

---

## 3. Large Modules & Complexity

### UI Automator Script
* **Issue**: [schedule_all_posts.cjs](file:///Users/anny/Downloads/Archives/instagram/schedule_all_posts.cjs) contains ~900 lines of complex browser automation logic, selector queries, custom wait routines, and DOM event overrides.
* **Impact**: High maintenance overhead. Small updates to LinkedIn's markup require refactoring this large file.
* **Fix**: Break the automation into smaller components (e.g. separation of authentication, post creation, and scheduling modules).
