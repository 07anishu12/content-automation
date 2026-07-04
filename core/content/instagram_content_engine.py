import json
from typing import Dict, List, Optional
from core.config import config
from core.services.llm_service import LLMService
from core.utils.json_helper import JsonHelper

class InstagramContentEngine:
    def __init__(self, niche: str = None, brand: str = None):
        self.niche = niche or config.TARGET_NICHE
        self.brand = brand or config.TARGET_BRAND
        self.llm = LLMService()

    def determine_format(self, topic_title: str, body: str) -> str:
        # Determine best format based on input content shape
        # Reels: best for quick punchy stories or dramatic contrarians
        # Carousel: best for multi-step listicles, how-to, or stats breakdowns
        # Infographic: best for comparisons, ranked lists, donut share splits
        body_lower = body.lower()
        if "vs" in topic_title.lower() or "comparison" in body_lower or "ranked" in body_lower:
            return "INFOGRAPHIC"
        elif len(body) > 300 or "step" in body_lower or "how to" in body_lower:
            return "CAROUSEL"
        elif "warning" in body_lower or "contrarian" in body_lower:
            return "REEL"
        else:
            return "STATIC_POST"

    def generate_content(self, topic_title: str, body: str, format_override: str = None) -> Dict:
        format_type = format_override or self.determine_format(topic_title, body)
        
        system_prompt = f"""You are a professional Instagram Content Strategist and Copywriter for the brand "{self.brand}" in the "{self.niche}" niche.
Your goal is to write high-performing Instagram content based on raw topic signals.
Your response must be a single, valid JSON object containing all requested fields.
Do NOT wrap your JSON in any markdown formatting or code blocks.
"""

        prompt = f"""Write an Instagram campaign for this topic:
Title: {topic_title}
Context: {body}

Target Format: {format_type}

You must return a valid JSON object matching this schema:
{{
  "format": "{format_type}",
  "post_text": "Write a highly engaging caption (max 1000 characters). Structure: Hook line -> Problem -> Solution value -> CTA question -> Follow CTA.",
  "hook": "Single punchy hook line to display on screen (max 8 words)",
  "cta": "Engagement call-to-action (e.g. 'Comment below if you agree!')",
  "hashtags": ["list", "of", "6", "relevant", "hashtags"],
  "keywords": ["tag", "metadata", "keywords"],
  "alt_text": "Accessibility alt text description of this post's theme.",
  "first_comment": "First comment block (e.g., resources links or supportive tags)",
  "pinned_comment": "Highlight comment to pin at top.",
  "carousel_slides": [
    {{
      "slide_num": 1,
      "header_label": "INTRO",
      "hook_part_1": "Slide 1 Hook Part 1",
      "hook_part_2": "Slide 1 Hook Part 2",
      "hook_emphasis": "EMPHASIZED WORD",
      "subtitle": "Brief intro description"
    }},
    {{
      "slide_num": 2,
      "pill_label": "STEP 1",
      "eyebrow": "PROCESS",
      "headline_part_1": "Headline part 1",
      "headline_part_2": "Headline part 2",
      "headline_emphasis": "EMPHASIS",
      "subhead": "Sub-element headline description",
      "body_text": "Body slide content. Keep sentences short."
    }}
  ],
  "infographic_data": {{
    "title_main": "Infographic Title",
    "title_span": "Italicized Accent Title",
    "subtitle": "Infographic description",
    "badge": "📊 DATA BREAKDOWN",
    "date_label": "2026 Report",
    "takeaway_num": "Hero Stat",
    "takeaway_text": "Hero stat context explanation",
    "source": "Source: {self.brand} | @{self.brand.lower()}",
    "bars": [
      {{ "label": "Metric Name 1", "value": "90%", "color": "#E63946" }},
      {{ "label": "Metric Name 2", "value": "60%", "color": "#5E6AD2" }}
    ]
  }},
  "reel_script": {{
    "visual_scene_1": "Describe what is shown on screen (e.g. founder pointing at EMI calculator)",
    "audio_script_1": "Spoken transcript voiceover words",
    "visual_scene_2": "Visual transition details",
    "audio_script_2": "Spoken voiceover script part 2"
  }}
}}

Make sure you write detailed copy for the target format {format_type}. If the format is CAROUSEL, output exactly 7 slides matching the schema. If it is INFOGRAPHIC, make sure to generate data points in 'bars'.
"""

        result_raw = self.llm.call_gemini(system_prompt, prompt, max_tokens=4000)
        return JsonHelper.parse_llm_json(result_raw)
