# Multi-Platform Content Automation

> A configurable automation platform for researching, generating, assembling, and scheduling branded content across LinkedIn and Instagram.

This project is an operations-focused content pipeline. It collects signals from configurable sources, turns selected topics into platform-specific copy and visual briefs, renders assets, and hands approved content to publishing adapters.

---

## 🛠️ Repository Layout

To maintain clear separation of concerns, the codebase is structured as follows:

```text
├── src/
│   ├── generators/  # LLM-assisted content, copy, and carousel compilers
│   ├── scrapers/    # RSS, Reddit, and API crawlers (Python/Puppeteer)
│   ├── automation/  # Puppeteer browser scripts for publishing and scheduling
│   └── utils/       # Slack webhook integrations, base64 encoders, and date helpers
├── templates/       # HTML infographic and carousel templates
├── data/            # Local JSON databases, cache, and scheduled logs
├── .env.example     # Environment configuration template
├── package.json     # Node.js workspace dependencies
└── README.md        # Documentation
```

---

## 🚀 Capabilities

*   **Configurable Research:** Crawls Reddit, RSS feeds, and news outlets for topical tech signals.
*   **LLM Content Generation:** Formulates platform-specific posts utilizing Gemini and Claude models.
*   **Visual Compilation:** Compiles custom HTML infographics and renders them using headless Chrome.
*   **Automated Scheduling:** Leverages Puppeteer scripts to schedule and post content to LinkedIn and Instagram platforms.
*   **Slack Integration:** Delivers notification digests and drafts for review.

---

## 📋 Prerequisites

*   Python 3.10+
*   Node.js 18+
*   An API Key for an LLM provider (Gemini or Claude)

---

## 🔨 Local Setup

1. Clone the repository and install npm packages:
   ```bash
   pnpm install
   ```
2. Set up environment variables:
   ```bash
   cp .env.example .env
   ```
3. Configure target sites, Slack webhooks, and AI provider credentials in `.env` (never commit this file).

4. Run the RSS crawler:
   ```bash
   python3 src/scrapers/fetch_ai_news_rss.py
   ```

5. Generate infographic images locally:
   ```bash
   python3 src/generators/gen_carousels.py
   ```

---

## 🔒 Security & Best Practices

*   **Least Privilege:** Ensure browser automation API keys use scoped permissions.
*   **Decoupled State:** Dynamic outputs and logs are maintained in `data/` to avoid polluting the core code.
*   **Credentials:** All credentials must remain in `.env` files.
