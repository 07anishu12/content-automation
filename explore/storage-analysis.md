# Storage Audit & Analysis

This document describes how data flows through the file system, detailing log files, temporary workspaces, and generated output locations.

---

## 1. Storage Locations & Directories

### Root Workspace (`/`)
* **Purpose**: Primary development area containing orchestration scripts and raw source databases.
* **Core Files**:
  * [reddit_data.json](file:///Users/anny/Downloads/Archives/instagram/reddit_data.json) (Scraped Reddit feeds)
  * [ai_news_data.json](file:///Users/anny/Downloads/Archives/instagram/ai_news_data.json) (Scraped news articles)
  * [linkedin-infographic.html](file:///Users/anny/Downloads/Archives/instagram/linkedin-infographic.html) (Infographic layout page)
  * [linkedin_posts_today.txt](file:///Users/anny/Downloads/Archives/instagram/linkedin_posts_today.txt) (Clean post texts)

### Temporary Folders
* **Path**: `carousel-routine/temp/carousel-branded/`
* **Purpose**: Holds individual slide HTML documents (`slide-0[1-7].html`) and local asset files (`assets/hero-ui.png`, `assets/interface.png`) during visual compilation.
* **Cleanup Pattern**: Files are overwritten or recreated during each run.

### Output Directories
* **Path**: `carousel-routine/output/YYYY-MM-DD/carousel-branded/`
* **Purpose**: Stores completed visual assets for archive purposes:
  * Individual slide PNGs (`slide-0[1-7].png`)
  * Slide composition wrapper (`carousel.html`)
  * Merged multi-page PDF (`linkedin-carousel-YYYY-MM-DD.pdf`)
* **Path**: `slack_downloads/`
* **Purpose**: Active publication directory. Holds finalized PDFs and PNGs for easy access by publishing scripts.

---

## 2. Dynamic State Logs (JSON Databases)

To maintain state and enforce deduplication, the system reads and appends to these three JSON logs in the root directory:

1. **[carousel-hook-log.json](file:///Users/anny/Downloads/Archives/instagram/carousel-hook-log.json)**:
   * Tracks recently used hook styles and formats.
   * Keeps a running history of the last 30 runs.
2. **[infographic-run-log.json](file:///Users/anny/Downloads/Archives/instagram/infographic-run-log.json)**:
   * Tracks used infographic topics and formats to prevent visual repetition.
   * Keeps a running history of the last 30 runs.
3. **[performance-run-log.json](file:///Users/anny/Downloads/Archives/instagram/performance-run-log.json)**:
   * Tracks subjects and categories for performance-engine posts.
   * Keeps a running history of the last 30 runs.

---

## 3. Storage Flow Diagram

```
[ Scrapers / RSS ] ──► write ──► [ Feeds JSON (Root) ]
                                         │
[ LLM Generation ] ──► write ──► [ Config JSONs (Root) ] & [ Text Drafts ]
                                         │
[ HTML Builders ]  ──► write ──► [ Temp HTMLs (carousel-routine/temp/) ]
                                         │
[ Puppeteer Render ] ──► write ──► [ Output PNGs/PDFs (carousel-routine/output/) ]
                                         │
[ Copy Command ]   ──► write ──► [ slack_downloads/ (Production Assets) ]
```
