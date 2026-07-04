# Data Flow Analysis

This document details the transformation states of content data as it traverses through the pipeline modules.

## Data Processing Lifecycle

```
[ Raw Reddit/RSS Data ]
         │
         ▼ (Fetch & filter out metadata)
[ Structured Feeds JSON ]
         │
         ▼ (Send to OpenRouter Chat Completions)
[ Raw Draft Posts + Visual Config JSON ]
         │
         ▼ (Automated revision loop via correct_posts.py)
[ Sanitized Post Texts ] ──────────────┐
         │                            │
         ▼ (Dynamic HTML generation)  │
[ Slide HTML Files ]                  │
         │                            │
         ▼ (Puppeteer screenshots)     │
[ Slide PNGs & Infographic PNG ]      │
         │                            │
         ▼ (Merge slide PNGs)         │
[ Carousel PDF ]                      │
         │                            │
         ├────────────────────────────┘
         ▼
[ Slack Channel Uploads ] ──► [ LinkedIn Dashboard scheduling ]
```

---

## Detailed Data Transformations

### 1. Scrape Output $\rightarrow$ Feeds JSON
* **Input**: Raw API payloads from Apify/RSS xml buffers.
* **Transformation**: The scraper cleans elements, filters out comments, selects required attributes (`title`, `selftext`/`body`, `permalink`/`url`, `score`/`ups`), and writes a clean JSON list.

### 2. Feeds JSON $\rightarrow$ Raw Text Drafts
* **Input**: Top 15 items in [reddit_data.json](file:///Users/anny/Downloads/Archives/instagram/reddit_data.json) and [ai_news_data.json](file:///Users/anny/Downloads/Archives/instagram/ai_news_data.json).
* **Transformation**: The LLM parses descriptions, maps topics against guidelines, drafts text, and structures output using separators:
  ```text
  ==================================================
  [POST HEADLINE / ID]
  ==================================================
  [POST BODY]
  ```

### 3. Raw Drafts $\rightarrow$ Sanitized Texts
* **Input**: [linkedin_posts_today.txt](file:///Users/anny/Downloads/Archives/instagram/linkedin_posts_today.txt).
* **Transformation**: The editor LLM reviews drafts, replaces any banned words (e.g., *leverage* $\rightarrow$ *use*), and inserts mandatory mentions of "FounderWing".

### 4. Visual Layout JSON $\rightarrow$ Rendered Slide HTML
* **Input**: [carousel_data.json](file:///Users/anny/Downloads/Archives/instagram/carousel_data.json) and [infographic_data.json](file:///Users/anny/Downloads/Archives/instagram/infographic_data.json).
* **Transformation**: HTML templates are loaded, replacement tags (e.g., `{{HOOK_PART_1}}`, `{{HUGE_STAT}}`) are replaced with JSON strings, and static HTML files are written.

### 5. Slide HTML $\rightarrow$ Compiled PDF
* **Input**: Slide HTML files.
* **Transformation**: Puppeteer loads slides, saves high-DPI screenshots, writes an HTML document containing image references, and prints it to PDF.

### 6. Clean Text + PDF/PNG $\rightarrow$ Slack / LinkedIn
* **Input**: Compiled files in `slack_downloads/`.
* **Transformation**: Files are posted to Slack via the files upload API, and Puppeteer inputs text and media files into the LinkedIn post creator.
