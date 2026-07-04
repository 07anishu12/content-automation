# Runtime Resource & Performance Analysis

This document describes the runtime resource consumption, timing bottlenecks, and optimization paths.

---

## 1. Timing Breakdown

A single execution run takes approximately **90 to 180 seconds**.

* **Fetch Phase**: **30 - 60s**. The scraping actors on Apify account for most of this time.
* **LLM Generation**: **15 - 30s**. Includes generating text completions and visual configurations.
* **Visual Rendering**: **20 - 45s**. Launching Chrome, screenshotting slide layouts, and merging them into a PDF.
* **LinkedIn Posting**: **20 - 45s**. Headless browser login, typing, file uploading, and scheduling.

---

## 2. Resource Consumption Metrics

* **CPU Usage**: Spawning headless Chrome instances via Puppeteer causes temporary CPU usage spikes.
* **Disk I/O**: High write counts in `/temp` directories during screenshot runs.
* **Network Overhead**: Data transfers for scraped feeds, LLM requests, and media file uploads.

---

## 3. Recommended Optimization Paths

* **Parallel Visual Screenshotting**: Capture slide screenshots in parallel using multiple browser tabs to reduce rendering time.
* **Reusing Chrome Context**: Reuse a single browser instance for both rendering and scheduling tasks.
* **API Scheduling**: Use API calls instead of browser automation where possible to reduce publishing overhead.
