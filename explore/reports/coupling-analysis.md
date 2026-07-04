# Component Coupling Analysis Report

This report evaluates class, function, and file coupling in the codebase.

---

## 1. Coupling Metrics

* **Content generation module**: [generate_all_content_gemini.py](file:///Users/anny/Downloads/Archives/instagram/generate_all_content_gemini.py) is tightly coupled to the layout structure of slide formats. Changes to the templates will require updating this generation script.
* **Asset compiler modules**: [generate_carousel_today.py](file:///Users/anny/Downloads/Archives/instagram/generate_carousel_today.py) and [build_carousel_today.cjs](file:///Users/anny/Downloads/Archives/instagram/build_carousel_today.cjs) are coupled. The JS script relies on the Python script running first to populate the slide template HTML files in the `/temp` directory.
* **Publishing module**: [schedule_all_posts.cjs](file:///Users/anny/Downloads/Archives/instagram/schedule_all_posts.cjs) has a tight dependency on the specific folder structure of `slack_downloads/`. It will fail to execute if file naming structures are modified.

---

## 2. Decoupling Recommendations

1. **Centralize Local File Paths**: Define output directories in a shared configuration file instead of using hardcoded paths across scripts.
2. **Standardize Visual Config Formats**: Define a common JSON structure for visuals data. This allows the asset builders to run independently of the LLM generation scripts.
3. **Decouple the Scheduling Layer**: Abstract the publisher into a generic interface (e.g. `SocialPublisher`). Specific implementation blocks (like `LinkedInPublisher` or `InstagramPublisher`) can then be swapped in without modifying other modules.
