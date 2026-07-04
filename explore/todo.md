# TODO List

List of tasks to complete the project migration to Instagram V2.

---

## 📅 High Priority
- [x] Implement generic config variables for target niche and branding templates.
- [x] Build the platform-independent `ResearchEngine` class.
- [x] Build `TopicIntelligence` script to score and rank scraped content topics.
- [x] Implement `InstagramContentEngine` to generate Posts, Stories, Quote Cards, Reels, and Carousels.
- [x] Build the `CaptionEngine` supporting CTA templates and alt-text generator.
- [x] Develop the custom `VisualsEngine` allowing configurable brand templates (Colors, logos).
- [x] Develop `InstagramPublisher` managing draft approval state sequences.
- [x] Create generic `AnalyticsEngine` data models.
- [x] Build V2 Master orchestrator script in root (`generate_instagram_campaign.py`).
- [x] Develop premium Instagram Portrait (1080x1350) template and Node compiler.
- [ ] Connect production cron runner to use `generate_instagram_campaign.py` daily.
