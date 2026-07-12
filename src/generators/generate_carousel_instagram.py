import os
import json
from core.config import config

def main():
    print("=== Generating Instagram Carousel Slide HTML Files ===")
    
    out_dir = os.path.join(config.ROOT_DIR, "carousel-routine/temp/carousel-branded")
    os.makedirs(out_dir, exist_ok=True)
    
    # Read the template
    template_path = os.path.join(config.ROOT_DIR, "adapters/instagram/assets/instagram-carousel-template.html")
    if not os.path.exists(template_path):
        print(f"Error: Template not found at {template_path}")
        return
        
    with open(template_path, "r", encoding="utf-8") as f:
        template_content = f.read()
        
    # Load dynamic carousel data
    json_path = os.path.join(config.ROOT_DIR, "carousel_data.json")
    carousel_data = {}
    if os.path.exists(json_path):
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                carousel_data = json.load(f)
            print("Loaded dynamic carousel slide data.")
        except Exception as e:
            print(f"Error loading carousel_data.json: {e}")
            
    brand_color = config.TARGET_BRAND_COLOR
    brand_name = config.TARGET_BRAND
    brand_handle = brand_name.lower()
    
    # Loop over 7 slides
    for i in range(1, 8):
        slide_num_str = str(i)
        slide_obj = carousel_data.get(slide_num_str, {})
        
        slide_html = template_content
        
        # Replace global brand details and styles
        slide_html = slide_html.replace("--brand-color: #E63946;", f"--brand-color: {brand_color};")
        slide_html = slide_html.replace("FOUNDERWING", brand_name.upper())
        slide_html = slide_html.replace("@founderswing", f"@{brand_handle}")
        slide_html = slide_html.replace("01 / 07", f"0{i} / 07")
        
        # Compile content
        if i == 1:
            # Hook title slide
            eyebrow = slide_obj.get("header_label") or slide_obj.get("pill_label") or "STRATEGY"
            hook_part_1 = slide_obj.get("hook_part_1") or "Instagram Growth"
            hook_part_2 = slide_obj.get("hook_part_2") or "frameworks for modern"
            hook_emphasis = slide_obj.get("hook_emphasis") or "Creators"
            subtitle = slide_obj.get("subtitle") or "A breakdown of step-by-step strategies to accelerate performance."
            
            content_block = f"""
            <div class="title-container">
                <div class="title-eyebrow">{eyebrow}</div>
                <h1 class="main-headline">{hook_part_1} {hook_part_2} <span class="highlight">{hook_emphasis}</span></h1>
                <p class="title-subtitle">{subtitle}</p>
            </div>
            """
        elif i == 7:
            # Outro slide
            content_block = f"""
            <div class="title-container" style="text-align: center;">
                <div class="title-eyebrow" style="margin-bottom: 30px;">OUTRO</div>
                <h1 class="main-headline" style="font-size: 58px; text-align: center;">Thanks for reading!</h1>
                <div class="card" style="margin-top: 40px; padding: 50px; text-align: center;">
                    <p class="card-body" style="font-size: 28px; font-weight: 700; color: #ffffff; line-height: 1.6;">
                        Follow <span style="color: var(--brand-color);">@{brand_handle}</span> for more strategic insights on {config.TARGET_NICHE}.
                    </p>
                </div>
            </div>
            """
            # Replace swipe indicator with simple end indicator
            slide_html = slide_html.replace("<span>Swipe Left</span>", "<span>Save Post</span>")
        else:
            # Content cards (Slides 2-6)
            pill = slide_obj.get("pill_label") or f"STEP 0{i-1}"
            headline_part_1 = slide_obj.get("headline_part_1") or slide_obj.get("eyebrow") or "Process Idea"
            headline_part_2 = slide_obj.get("headline_part_2") or ""
            headline_emphasis = slide_obj.get("headline_emphasis") or ""
            body_text = slide_obj.get("body_text") or slide_obj.get("subhead") or ""
            
            content_block = f"""
            <div class="card">
                <div class="card-header">
                    <div class="card-number">0{i-1}</div>
                    <h2 class="card-title">{headline_part_1} {headline_part_2} <span style="color: var(--brand-color);">{headline_emphasis}</span></h2>
                </div>
                <div class="card-body">
                    {body_text}
                </div>
            </div>
            """
            
        # Inject main content block into template body placeholder
        slide_html = slide_html.replace('<main id="slide-content">\n        <!-- Dynamic content injected here -->\n        <div class="title-container">\n            <div class="title-eyebrow" id="eyebrow">STRATEGY</div>\n            <h1 class="main-headline" id="headline">How to build an <span class="highlight">Unfair</span> <span class="italic-accent">Advantage</span></h1>\n            <p class="title-subtitle" id="subtitle">The frameworks top founders use to scale from zero to millions.</p>\n        </div>\n    </main>', f'<main id="slide-content">{content_block}</main>')
        
        # Alternative simple search-replace just in case spacing differs
        if '<main id="slide-content">' in slide_html and content_block not in slide_html:
            # If standard long replace failed, replace the whole main block
            slide_html = re.sub(r'<main id="slide-content">.*?</main>', f'<main id="slide-content">{content_block}</main>', slide_html, flags=re.DOTALL)
            
        slide_out_path = os.path.join(out_dir, f"slide{i}.html")
        with open(slide_out_path, "w", encoding="utf-8") as f:
            f.write(slide_html)
            
    print("Successfully generated all 7 slide HTML files.")

if __name__ == "__main__":
    main()
