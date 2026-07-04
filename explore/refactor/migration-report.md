# V2 Pipeline Migration Report (LinkedIn → Instagram)

This report details the work done to convert the legacy LinkedIn content automation scripts into a generic, multi-niche Instagram campaign platform.

---

## 1. Replaced Components

* **Visual Asset Layouts**:
  * *LinkedIn (Legacy)*: `generate_carousel_today.py` and `build_carousel_today.cjs` compiled landscape/square slides using `/Users/prithal/...` absolute paths.
  * *Instagram (New V2)*: `generate_carousel_instagram.py` and `build_carousel_instagram.cjs` compile **1080x1350 vertical aspect ratio Portrait slides** using a modern glassmorphism template without external absolute path dependencies.
* **Publishing / Review Flow**:
  * *LinkedIn (Legacy)*: Puppeteer scripts (`schedule_all_posts.cjs`, etc.) automated desktop browser clicks.
  * *Instagram (New V2)*: `InstagramPublisherAdapter` delivers structured visual campaigns (caption, tags, and generated asset files) directly to Slack for manual reviews and approvals.
* **Research and Signal Scraping**:
  * *LinkedIn (Legacy)*: Locked to specific AI-related subreddits.
  * *Instagram (New V2)*: Dynamic topic mapping based on the configured niche (SaaS, Fitness, AI, Travel, Finance). Scrapes target RSS news resources if Reddit blocks requests.

---

## 2. Decoupled Core Design Summary
* **Configurable branding**: Font style and color attributes are defined in a single file and injected dynamically into layout templates at compilation.
* **No hardcoded content rules**: Prompts and models are decoupled so that targeting a new business niche only requires editing `TARGET_NICHE` configuration.
