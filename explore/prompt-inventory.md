# Prompt Inventory

This document inventories the AI prompts used throughout the content generation pipeline.

---

## 1. Writing Rules & Style Constraints Prompt
* **Location**: [generate_all_content_gemini.py](file:///Users/anny/Downloads/Archives/instagram/generate_all_content_gemini.py#L91)
* **Purpose**: Implements the tone, vocabulary filters, structure, and constraints for all generated posts.
* **Input**: Standard style directives (e.g., third-person voice, sentence-case headings, no em-dashes).
* **Output**: Text drafts that adhere to the style guide.
* **Banned Words List**: Includes terms like *delve*, *underscore*, *tapestry*, *interplay*, *leverages*, *supercharge*, and *revolutionary*.
* **Banned LinkedIn Patterns**: Buns phrases like *"No X. No Y. Just Z."* and *"It's not just about X. It's about Y."*

---

## 2. 11 Main Posts Generation Prompts
* **Location**: [generate_all_content_gemini.py](file:///Users/anny/Downloads/Archives/instagram/generate_all_content_gemini.py#L123-L233)
* **Purpose**: Prompts the LLM to write 11 specific post drafts:
  1. **Collaborative Article**: subcontractor service business cash flow.
  2. **Poll**: Tier-1 MBA vs building startup directly.
  3. **Carousel**: Dorm room founder journey (before-after style).
  4. **Infographic Caption**: Focus fragmentation (Microsoft Work Trend Index data).
  5. **Post 1 (Tool Spotlight)**: Deezer AI music detector.
  6. **Post 2 (Weekly Roundup)**: 4 major tech updates (Manus AI, Jeff Bezos's Prometheus, KPMG AI retraction, Theker Factory Robot).
  7. **Post 3 (Plain English Breakdown)**: Jeff Bezos's Prometheus 12 billion dollar raise.
  8. **Post 4 (Unfair Advantage)**: Theker's factory robot.
  9. **Post 5 (Career/Income)**: KPMG AI usage retraction.
  10. **Post 6 (Hot Take)**: Meta's AI engineering culture.
  11. **Post 7 (Steal This)**: Two-agent audit loop prompt workflow.
* **Output Format**: Clean copy, starting directly with the hook, without bold titles or labels.

---

## 3. Carousel JSON Structure Prompt
* **Location**: [generate_all_content_gemini.py](file:///Users/anny/Downloads/Archives/instagram/generate_all_content_gemini.py#L267-L339)
* **Purpose**: Translates the generated text carousel draft into a structured JSON configuration matching the slide layout templates.
* **Input**: Content drafted for Post 3.
* **Expected JSON Output**:
  ```json
  {
    "1": { "HEADER_LABEL": "...", "HOOK_PART_1": "...", "HOOK_PART_2": "...", "HOOK_EMPHASIS": "...", "SUBTITLE": "..." },
    "2": { "PILL_LABEL": "...", "EYEBROW": "...", "HEADLINE_PART_1": "...", "HEADLINE_PART_2": "...", "HEADLINE_EMPHASIS": "...", "SUBHEAD": "...", "BODY_TEXT": "..." },
    "...": "..."
  }
  ```

---

## 4. Infographic JSON Structure Prompt
* **Location**: [generate_all_content_gemini.py](file:///Users/anny/Downloads/Archives/instagram/generate_all_content_gemini.py#L363-L390)
* **Purpose**: Generates structured JSON parameters for rendering the HTML infographic based on the Microsoft Trend data.
* **Input**: Content drafted for Post 4.
* **Expected JSON Output**:
  ```json
  {
    "title_main": "The Daily Workplace Noise Index",
    "title_span": "Workplace Interruption Stats",
    "subtitle": "...",
    "badge": "📊 WORKPLACE NOISE",
    "date_label": "2025 Microsoft Report",
    "takeaway_num": "2 Mins",
    "takeaway_text": "...",
    "source": "Source: Microsoft Work Trend Index | @founderswing",
    "bars": [
      { "label": "...", "value": "...", "color": "..." }
    ]
  }
  ```

---

## 5. 5 Performance Posts Prompts
* **Location**: [generate_all_content_gemini.py](file:///Users/anny/Downloads/Archives/instagram/generate_all_content_gemini.py#L415-L467)
* **Purpose**: Generates 5 analytics-driven posts modeled after previous top performers:
  1. **Founder Psychology Contrarian**: Banning talking about your startup before it's real.
  2. **Loaded Poll**: Best way to validate a startup idea.
  3. **AI News + Implications**: KPMG AI retraction implications.
  4. **Story Carousel**: Copying an existing local business vs inventing one.
  5. **Data Visual + Hook**: Interruption stats with communication overload theme.

---

## 6. Text Editor Correction Prompt
* **Location**: [correct_posts.py](file:///Users/anny/Downloads/Archives/instagram/correct_posts.py#L30-L48)
* **Purpose**: Polishes the draft text to programmatically ensure word limits, insert mandatory brand references ("FounderWing"), and replace any remaining banned words.
* **Input**: Raw text from [linkedin_posts_today.txt](file:///Users/anny/Downloads/Archives/instagram/linkedin_posts_today.txt).
* **Output**: Corrected, clean text output block.
