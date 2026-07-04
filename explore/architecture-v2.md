# Instagram Automation Platform Architecture (V2)

This document details the target design of the Instagram content campaign engine.

## Component Layout (V2)

```
                       ┌─────────────────────────┐
                       │     ORCHESTRATOR        │ (e.g. generate_instagram_campaign.py)
                       └────────────┬────────────┘
                                    │
         ┌──────────────────────────┼──────────────────────────┐
         ▼                          ▼                          ▼
┌─────────────────┐        ┌─────────────────┐        ┌─────────────────┐
│ Research Engine │        │ Content Engine  │        │ Visuals Engine  │
│ (Niche-agnostic)│        │ (Reels/Stories/ │        │ (Configurable   │
│                 │        │ Carousels/etc.) │        │ branding assets)│
└─────────────────┘        └─────────────────┘        └─────────────────┘
```

### Decoupled Core Components
1. **Configurable Niche System**: Environment configurations specify target niche/keywords and branding styles, allowing the engine to adapt dynamically.
2. **Topic Scoring**: Scraped topics are ranked using trend strength, business value, and relevance metrics.
3. **Structured Captions**: Generates hashtags, alt-text, and comment blocks dynamically alongside the post body.
4. **Visual rendering**: Exports visual assets tailored to Instagram's feed formats (1:1/4:5 images and 9:16 vertical video cover layouts).
