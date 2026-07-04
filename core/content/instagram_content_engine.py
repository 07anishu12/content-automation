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
        parsed = JsonHelper.parse_llm_json(result_raw) if result_raw else None
        
        if not parsed:
            print("Warning: OpenRouter call failed or returned empty. Using premium mockup fallback...")
            parsed = {
                "format": format_type,
                "post_text": f"🚀 Big shifts in {self.niche}: {topic_title}. This changes how we build products. Here is a quick breakdown. What do you think?",
                "hook": f"The New Era of {self.niche}",
                "cta": "Comment below with your thoughts!",
                "hashtags": [self.niche.replace(" ", ""), "automation", "strategy", "growth", "founder"],
                "keywords": [self.niche.lower(), "marketing"],
                "alt_text": f"Text slides describing: {topic_title}",
                "first_comment": "Link in bio to read the full report!",
                "pinned_comment": "Subscribe to our daily updates.",
                "carousel_slides": [
                    {
                        "slide_num": 1,
                        "header_label": "BREAKDOWN",
                        "hook_part_1": topic_title[:25],
                        "hook_part_2": "Why this changes",
                        "hook_emphasis": "Everything",
                        "subtitle": "A step-by-step impact guide."
                    },
                    {
                        "slide_num": 2,
                        "pill_label": "THE SHIFT",
                        "eyebrow": "CONTEXT",
                        "headline_part_1": "Google's search shift",
                        "headline_part_2": "is moving traffic to",
                        "headline_emphasis": "AI agents",
                        "body_text": "If users get answers directly in the search box, your website clicks will drop. You need to optimize for AI references."
                    },
                    {
                        "slide_num": 3,
                        "pill_label": "STEP 1",
                        "eyebrow": "STRATEGY",
                        "headline_part_1": "Optimize for",
                        "headline_part_2": "LLM visibility and",
                        "headline_emphasis": "citations",
                        "body_text": "Include clean structured schemas on your landing page so models like Gemini and ChatGPT index your content directly."
                    },
                    {
                        "slide_num": 4,
                        "pill_label": "STEP 2",
                        "eyebrow": "DISTRIBUTION",
                        "headline_part_1": "Build direct to",
                        "headline_part_2": "consumer media",
                        "headline_emphasis": "channels",
                        "body_text": "Relying on SEO is a dying playbook. Transition to email newsletters and social communities where you own the audience."
                    },
                    {
                        "slide_num": 5,
                        "pill_label": "STEP 3",
                        "eyebrow": "PRODUCT",
                        "headline_part_1": "Embed search",
                        "headline_part_2": "directly inside your",
                        "headline_emphasis": "UI/UX",
                        "body_text": "Create simple tool hooks that deliver immediate value to users so they don't have to search Google to solve their problems."
                    },
                    {
                        "slide_num": 6,
                        "pill_label": "SUMMARY",
                        "eyebrow": "TAKEAWAY",
                        "headline_part_1": "Adapt your",
                        "headline_part_2": "growth loop for the",
                        "headline_emphasis": "AI age",
                        "body_text": "Focus on high-quality content, direct distribution, and indexing optimization."
                    },
                    {
                        "slide_num": 7,
                        "header_label": "OUTRO",
                        "hook_part_1": "Ready to scale?",
                        "hook_part_2": "Follow for more breakdowns",
                        "hook_emphasis": "Daily",
                        "subtitle": f"Join our community of builders and founders."
                    }
                ],
                "infographic_data": {
                    "title_main": "Google Search Changes",
                    "title_span": "Redesign stats",
                    "subtitle": "How the new search layout shifts organic click-through rates.",
                    "badge": "📊 ORGANIC TRAFFIC",
                    "date_label": "2026 Analysis",
                    "takeaway_num": "45%",
                    "takeaway_text": "Drop in organic web traffic expected for standard blogs over the next 18 months.",
                    "source": f"Source: {self.brand} | @{self.brand.lower()}",
                    "bars": [
                        { "label": "AI Overview Clicks", "value": "78%", "color": config.TARGET_BRAND_COLOR },
                        { "label": "Direct Product Queries", "value": "55%", "color": "#5E6AD2" },
                        { "label": "Traditional Blog Traffic", "value": "22%", "color": "#5A5A5A" }
                    ]
                },
                "reel_script": {
                    "visual_scene_1": "Founder looking shocked at a Google Search page on monitor.",
                    "audio_script_1": "Google just did the unthinkable. They redesigned their search box after 25 years.",
                    "visual_scene_2": "Transition to graphic showing zero-click searches statistics.",
                    "audio_script_2": "Here's what it means for your business: organic traffic is shifting entirely to AI citations."
                }
            }
        return parsed
