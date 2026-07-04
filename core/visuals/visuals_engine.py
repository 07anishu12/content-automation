import os
import json
import re
import subprocess
from core.config import config

class VisualsEngine:
    def __init__(self, brand_name: str = None, brand_color: str = None):
        self.brand_name = brand_name or config.TARGET_BRAND
        self.brand_color = brand_color or config.TARGET_BRAND_COLOR
        self.temp_dir = os.path.join(config.ROOT_DIR, "carousel-routine/temp/carousel-branded")
        os.makedirs(self.temp_dir, exist_ok=True)

    def write_infographic_html(self, info_data: dict, template_path: str = None) -> str:
        temp_path = template_path or os.path.join(config.ROOT_DIR, "linkedin-infographic-template.html")
        if not os.path.exists(temp_path):
            # Fallback simple template
            html_content = f"""
            <html>
            <body style="background:#F5EFE8; font-family:sans-serif; padding:40px; margin:0; width:1080px; height:1080px; box-sizing:border-box;">
                <div style="font-size:42px; font-weight:800; color:#1A1A1A;">{info_data.get("title_main", "Statistics")}</div>
                <div style="font-size:24px; color:#5A5A5A; margin-top:10px;">{info_data.get("subtitle", "")}</div>
                <div class="chart" style="margin-top:60px;">
                    <!-- BARS_CONTAINER -->
                </div>
                <div style="position:absolute; bottom:40px; width:1000px; display:flex; justify-content:space-between; font-size:16px; color:#5A5A5A;">
                    <span>{info_data.get("source", "")}</span>
                    <span>@{self.brand_name.lower()}</span>
                </div>
            </body>
            </html>
            """
        else:
            with open(temp_path, "r", encoding="utf-8") as f:
                html_content = f.read()

        # Apply branding modifications
        html_content = html_content.replace("#E63946", self.brand_color)
        html_content = html_content.replace("@founderswing", f"@{self.brand_name.lower()}")
        
        # Merge key title values
        html_content = html_content.replace("The Daily Workplace Noise Index", info_data.get("title_main", "Index"))
        html_content = html_content.replace("Workplace Interruption Stats", info_data.get("title_span", "Stats"))
        html_content = html_content.replace("How the constant stream of emails, chats, and meetings fragments the modern workday.", info_data.get("subtitle", ""))
        html_content = html_content.replace("📊 WORKPLACE NOISE", info_data.get("badge", ""))
        html_content = html_content.replace("2025 Microsoft Report", info_data.get("date_label", ""))
        html_content = html_content.replace("2 Mins", info_data.get("takeaway_num", ""))
        html_content = html_content.replace("is the average time between interruptions for a typical employee, leading to focus fragmentation.", info_data.get("takeaway_text", ""))
        html_content = html_content.replace("Source: Microsoft Work Trend Index | @founderswing", info_data.get("source", f"Source: {self.brand_name} | @{self.brand_name.lower()}"))

        # Build dynamic bars
        bars = info_data.get("bars", [])
        bars_html = ""
        for i, bar in enumerate(bars):
            num = f"0{i+1}" if i < 9 else f"{i+1}"
            bars_html += f"""
            <div class="row" style="display: flex; align-items: center; margin-bottom: 20px; font-family: sans-serif;">
                <div class="num" style="font-style: italic; font-size: 32px; width: 40px; color: {self.brand_color};">{num}</div>
                <div class="bar-container" style="flex: 1; background: #E2DCD5; height: 35px; border-radius: 18px; margin: 0 15px; overflow: hidden; position: relative;">
                    <div class="bar" style="width: {bar.get('value', '50%')}; background: {bar.get('color', self.brand_color)}; height: 100%; border-radius: 18px; display: flex; align-items: center; padding-left: 15px;">
                        <span style="font-weight: 700; color: #1A1A1A; font-size: 14px;">{bar.get('label', '')}</span>
                    </div>
                </div>
                <div class="val" style="font-weight: 700; color: #1A1A1A; font-size: 20px; width: 60px; text-align: right;">{bar.get('value', '')}</div>
            </div>
            """

        if "<!-- BARS_CONTAINER -->" in html_content:
            html_content = html_content.replace("<!-- BARS_CONTAINER -->", bars_html)
        else:
            # Fallback search injection
            html_content = html_content.replace('<div class="chart">', f'<div class="chart">{bars_html}')

        output_path = os.path.join(config.ROOT_DIR, "linkedin-infographic.html")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        return output_path

    def build_carousel_slides(self, slides_data: list) -> bool:
        # Write slide configs to JSON for the compiler
        json_path = os.path.join(config.ROOT_DIR, "carousel_data.json")
        slides_dict = {str(i+1): slide for i, slide in enumerate(slides_data)}
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(slides_dict, f, indent=2)

        # Run generator to build slide HTML files
        try:
            generator_script = os.path.join(config.ROOT_DIR, "generate_carousel_instagram.py")
            subprocess.run(["python3", generator_script], check=True)
            return True
        except Exception as e:
            print(f"Error building carousel slides HTML: {e}")
            return False

    def compile_assets(self) -> bool:
        # Render PNGs and PDF using Puppeteer
        try:
            compiler_script = os.path.join(config.ROOT_DIR, "build_carousel_instagram.cjs")
            subprocess.run(["node", compiler_script], check=True)
            
            # Screenshot infographic
            cap_script = os.path.join(config.ROOT_DIR, "cap_infographic_today.cjs")
            subprocess.run(["node", cap_script], check=True)
            return True
        except Exception as e:
            print(f"Error compiling visual assets via Puppeteer: {e}")
            return False
