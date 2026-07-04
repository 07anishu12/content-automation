# Prompts Inventory File

This file lists the exact system prompt paths and configurations in the repository.

| Prompt Name | Target Location | Model Used | Output Format | Banned Vocab Filters |
|---|---|---|---|---|
| **Style & Writing System** | [generate_all_content_gemini.py](file:///Users/anny/Downloads/Archives/instagram/generate_all_content_gemini.py#L91) | Gemma-31b-it | String | 50+ corporate terms |
| **11 Main LinkedIn Posts** | [generate_all_content_gemini.py](file:///Users/anny/Downloads/Archives/instagram/generate_all_content_gemini.py#L123) | Gemma-31b-it | Raw text block | Banned patterns |
| **Carousel Structured JSON** | [generate_all_content_gemini.py](file:///Users/anny/Downloads/Archives/instagram/generate_all_content_gemini.py#L267) | Gemma-31b-it | Structured JSON | No Markdown blocks |
| **Infographic Stats JSON** | [generate_all_content_gemini.py](file:///Users/anny/Downloads/Archives/instagram/generate_all_content_gemini.py#L363) | Gemma-31b-it | Structured JSON | Color hex validation |
| **5 Performance Posts** | [generate_all_content_gemini.py](file:///Users/anny/Downloads/Archives/instagram/generate_all_content_gemini.py#L415) | Gemma-31b-it | Raw text block | Observational voice |
| **Post revision editor** | [correct_posts.py](file:///Users/anny/Downloads/Archives/instagram/correct_posts.py#L30) | Gemma-31b-it | Raw text block | Brand mentions insert |

### Key Guidelines Programmed in Prompts:
* **The "Varun Mayya of LinkedIn" Doctrine**: Focuses content on high-altitude AI impacts (work, career, automation stats) rather than coding tutorials.
* **Negative Prompt Constraints**: Excludes terms like *delve*, *leverage*, *tapestry*, *interplay*, and *revolutionary*.
* **JSON Output Formatting**: Instructs the model to return raw JSON objects without wrapping them in markdown block ticks, preventing JSON parsing exceptions at runtime.
