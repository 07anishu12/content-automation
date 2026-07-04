# Folders Inventory

This document details the folders in the codebase.

---

## 1. [carousel-routine/](file:///Users/anny/Downloads/Archives/instagram/carousel-routine)
Node.js workspace that compiles HTML/CSS slides to PNGs and PDFs using Puppeteer.
* **[temp/](file:///Users/anny/Downloads/Archives/instagram/carousel-routine/temp)**: Stores individual slide HTML templates before rendering.
* **[output/](file:///Users/anny/Downloads/Archives/instagram/carousel-routine/output)**: Stores completed slide PNGs and PDF carousels.

---

## 2. [skills/](file:///Users/anny/Downloads/Archives/instagram/skills)
Houses prompt templates and instruction files that guide the LLM's drafting logic.
* **[branded-carousel/](file:///Users/anny/Downloads/Archives/instagram/skills/branded-carousel)**: Prompts for researching brand identities and designing layouts.
* **[illustration-formats/](file:///Users/anny/Downloads/Archives/instagram/skills/illustration-formats)**: HTML templates for infographic formats.
* **[linkedin-ai-news-engine/](file:///Users/anny/Downloads/Archives/instagram/skills/linkedin-ai-news-engine)**: Prompt instructions for drafting AI news posts.
* **[linkedin-performance-engine/](file:///Users/anny/Downloads/Archives/instagram/skills/linkedin-performance-engine)**: Prompts designed to replicate top-performing post patterns from account history.

---

## 3. [commands/](file:///Users/anny/Downloads/Archives/instagram/commands)
Defines low-level syntax constraints (e.g., banning em-dashes) and styling directives that the LLM drafts must adhere to.

---

## 4. [daily-linkedin-posts/](file:///Users/anny/Downloads/Archives/instagram/daily-linkedin-posts)
Contains orchestration routines that specify how to run the pipeline phases step-by-step.
