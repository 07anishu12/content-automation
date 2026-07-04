# Folder Structure

This document catalogs every directory and explains the role of key folders in the system.

## Project Structure Overview

```
instagram/ (Root)
├── carousel-routine/      <-- Node.js environment to compile HTML/CSS to PDF
│   ├── temp/              <-- Slide HTML files are written here during runtime
│   └── output/            <-- Rendered slide PNGs and completed PDFs
│
├── skills/                <-- Specialized prompt templates & asset configs
│   ├── branded-carousel/  <-- Dynamic carousel layouts & visual templates
│   ├── illustration-formats/ <-- HTML infographic recipes & styles
│   ├── linkedin-ai-news-engine/ <-- Instructions to draft AI newsletter posts
│   └── linkedin-performance-engine/ <-- Analytics-driven templates
│
├── commands/              <-- Low-level formatting rules & banned word lists
│
├── daily-linkedin-posts/  <-- Pipeline orchestration routines
│
├── sample-outputs/        <-- Example outputs & assets
│
└── explore/               <-- Codebase audit & documentation directory
```

---

## Detailed Directory Breakdown

### 1. Root Directory (`/`)
Houses the main Python scripts that coordinate data fetching, LLM integration, post cleaning, and Node.js Puppeteer scripts that handle scheduling and image rendering.

### 2. [carousel-routine/](file:///Users/anny/Downloads/Archives/instagram/carousel-routine)
Contains Node.js libraries and scripts that compile individual slide HTML templates into PNGs using Puppeteer, then combine those PNGs into a multi-page PDF using `pdf-lib`.

### 3. [skills/](file:///Users/anny/Downloads/Archives/instagram/skills)
Houses prompt templates and instruction files that guide the LLM's drafting logic.
* **[branded-carousel/](file:///Users/anny/Downloads/Archives/instagram/skills/branded-carousel)**: Defines the visual look of dynamic slides and outlines research instructions for retrieving company logo/colors.
* **[illustration-formats/](file:///Users/anny/Downloads/Archives/instagram/skills/illustration-formats)**: Contains HTML templates for infographic formats.
* **[linkedin-ai-news-engine/](file:///Users/anny/Downloads/Archives/instagram/skills/linkedin-ai-news-engine)**: Prompt settings to draft posts based on news articles.
* **[linkedin-performance-engine/](file:///Users/anny/Downloads/Archives/instagram/skills/linkedin-performance-engine)**: Prompts designed to replicate top-performing post patterns from account history.

### 4. [commands/](file:///Users/anny/Downloads/Archives/instagram/commands)
Defines low-level syntax constraints (e.g., banning em-dashes) and styling directives that the LLM drafts must adhere to.

### 5. [daily-linkedin-posts/](file:///Users/anny/Downloads/Archives/instagram/daily-linkedin-posts)
Contains orchestration routines that specify how to run the pipeline phases step-by-step.
