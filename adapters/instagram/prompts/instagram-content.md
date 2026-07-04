# Instagram Content & Formatting Guidelines

This document defines the content guidelines, prompts, and templates for generating high-performance Instagram content across any configurable niche.

---

## 📸 Content Strategy by Format

Instagram is a visual-first platform. Content should be positioned to capture attention immediately, break down complex topics into digestible steps, and invite engagement.

### 1. Carousel Posts
* **Objective**: Educational slides mapping a step-by-step process, comparison, or framework.
* **Layout**: Exactly 7 slides.
  * *Slide 1 (Hook)*: Bold visual hook, brand logo, swipe indicator.
  * *Slides 2-6 (Value)*: One clear insight per slide. Keep body text under 40 words per slide.
  * *Slide 7 (Outro/CTA)*: Clear follow call-to-action, profile tag, like/save reminder.

### 2. Infographic Posts
* **Objective**: Ranked lists, comparison tables, or donut splits displaying real data.
* **Layout**: Vertical 1080x1350 visual displaying 3 to 6 ranked bars or rows.
* **Metrics**: Accompanying takeaway hero stat and clear source metadata.

### 3. Reels Scripts
* **Objective**: Short, punchy vertical video script with visual scene directions.
* **Structure**: Visual Hook (0-3s) -> Direct Problem -> Spoken value beats -> Soundbite -> Visual call-to-action (CTA).

### 4. Quote Cards
* **Objective**: High-relevance, thought-provoking single sentences.
* **Layout**: Minimalist layout with large quotation text and signature handle.

---

## ✍️ Copywriting Rules (Caption Engine)

When generating captions and text parameters, adhere to the following rules:

1. **The Hook**: Maximum 8 words. Must create curiosity or outline a high-stakes problem immediately.
2. **Body Text**: Break into short 1-line paragraphs with spacing. Use bullet points and emojis sparingly. Keep total length under 1000 characters.
3. **The call-to-action (CTA)**: Invite specific actions (e.g. "Save this for later," "Comment your thoughts below").
4. **Hashtags**: Exactly 6 targeted hashtags. Mix 3 broad niche terms (e.g. `#finance`) and 3 specific sub-theme terms (e.g. `#emicalculator`).
5. **Alt Text**: Clear, descriptive accessibility text explaining the visual elements of the slide deck.

---

## 🛠️ JSON Schema Contract

All Instagram creative generators must output valid JSON conforming to this target structure:

```json
{
  "format": "CAROUSEL | INFOGRAPHIC | REEL | STATIC_POST",
  "post_text": "Engaging caption copy with clear line breaks.",
  "hook": "Punchy slide title / hook line.",
  "cta": "Call to action text.",
  "hashtags": ["tag1", "tag2", "tag3", "tag4", "tag5", "tag6"],
  "keywords": ["key1", "key2"],
  "alt_text": "Accessibility text description.",
  "first_comment": "First comment text.",
  "pinned_comment": "Pinned header comment.",
  "carousel_slides": [
    {
      "slide_num": 1,
      "header_label": "INTRO",
      "hook_part_1": "Bold Title Line",
      "hook_part_2": "Supporting Title Line",
      "hook_emphasis": "EMPHASIZED WORD",
      "subtitle": "Brief subtitle description."
    }
  ],
  "infographic_data": {
    "title_main": "Main Title",
    "title_span": "Italic Accent",
    "subtitle": "Supporting description",
    "badge": "📊 DATA STATS",
    "date_label": "2026",
    "takeaway_num": "Hero value",
    "takeaway_text": "Description of hero value",
    "source": "Source citation",
    "bars": [
      { "label": "Label 1", "value": "80%", "color": "#HEX" }
    ]
  },
  "reel_script": {
    "visual_scene_1": "Scene visual context description",
    "audio_script_1": "Voiceover spoken text"
  }
}
```
