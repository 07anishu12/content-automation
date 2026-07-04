# Runtime Sequence

This document describes the runtime sequence diagram details for a complete cycle.

## Sequenced Events

```
  [ Fetch Phase ]
1. Run fetch_reddit_apify.py
   ↳ Request to Apify Runs API
   ↳ Polling status (GET /v2/actor-runs)
   ↳ Fetch items (GET /v2/datasets)
   ↳ Write reddit_data.json
2. Run fetch_ai_news_rss.py
   ↳ Fetch VentureBeat/TechCrunch XML
   ↳ Parse RSS items using ET.fromstring
   ↳ Clean descriptions
   ↳ Write ai_news_data.json

  [ Content Generation Phase ]
3. Run generate_all_content_gemini.py
   ↳ Load reddit_data.json & ai_news_data.json
   ↳ Request OpenRouter (google/gemma-4-31b-it:free) for 11 posts
   ↳ Request OpenRouter for Carousel JSON slide config
   ↳ Request OpenRouter for Infographic JSON config
   ↳ Write: linkedin_posts_today.txt, carousel_data.json, infographic_data.json
4. Run correct_posts.py
   ↳ Read linkedin_posts_today.txt
   ↳ Send to OpenRouter for word cleanup and Brand check
   ↳ Overwrite linkedin_posts_today.txt with clean text

  [ Visual Compiler Phase ]
5. Run build_carousel_today.cjs
   ↳ Execute generate_carousel_today.py
     ↳ Read SKILL.md templates
     ↳ Merge carousel_data.json fields into templates
     ↳ Save temp HTML slides in temp/
   ↳ Puppeteer launches Chrome
   ↳ Navigate to slides HTML, screenshot to PNG
   ↳ Write image refs to carousel.html
   ↳ Print page to PDF -> linkedin-carousel-YYYY-MM-DD.pdf
6. Run generate_infographic_today.py
   ↳ Read template HTML
   ↳ Merge infographic_data.json fields
   ↳ Write linkedin-infographic.html
7. Run cap_infographic_today.cjs
   ↳ Puppeteer launches Chrome
   ↳ Navigate to linkedin-infographic.html
   ↳ Screenshot to PNG -> linkedin-infographic-YYYYMMDD.png

  [ Publishing Phase ]
8. Run send_to_slack.py
   ↳ Post clean texts
   ↳ Upload Carousel PDF to Slack API
   ↳ Upload Infographic PNG to Slack API
9. Run schedule_all_posts.cjs
   ↳ Launch Chrome session via Puppeteer
   ↳ Navigate to LinkedIn dashboard
   ↳ Open posting modal, fill text and attach assets
   ↳ Schedule post at designated slot
   ↳ Update logs: carousel-hook-log.json, etc.
```
