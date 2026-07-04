import os

def load_env(env_path="./.env"):
    env_vars = {}
    if os.path.exists(env_path):
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                stripped = line.strip()
                if "=" in stripped and not stripped.startswith("#"):
                    k, v = stripped.split("=", 1)
                    env_vars[k.strip()] = v.strip()
    return env_vars

_env_dict = load_env()

# API Keys and Tokens
OPENROUTER_API_KEY = _env_dict.get("OPENROUTER_API_KEY") or os.getenv("OPENROUTER_API_KEY")
APIFY_API_KEY = _env_dict.get("APIFY_API_KEY") or os.getenv("APIFY_API_KEY")
SLACK_BOT_TOKEN = _env_dict.get("SLACK_BOT_TOKEN") or os.getenv("SLACK_BOT_TOKEN")
SCRAPINGDOG_API_KEY = _env_dict.get("SCRAPINGDOG_API_KEY") or os.getenv("SCRAPINGDOG_API_KEY")
ANTHROPIC_API_KEY = _env_dict.get("ANTHROPIC_API_KEY") or os.getenv("ANTHROPIC_API_KEY") or _env_dict.get("ANTHROPIC_TOKEN") or os.getenv("ANTHROPIC_TOKEN")
GEMINI_API_KEY = _env_dict.get("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY")

# Services Configuration
SLACK_CHANNEL = "C0AVBBTD529"
OPENROUTER_MODEL = "google/gemma-4-31b-it:free"
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

# System Paths & Constants
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
DOWNLOADS_DIR = "/Users/prithal/Downloads" if os.path.exists("/Users/prithal/Downloads") else os.path.expanduser("~/Downloads")

# Niche & Brand Configuration
TARGET_NICHE = _env_dict.get("TARGET_NICHE") or os.getenv("TARGET_NICHE") or "Artificial Intelligence"
TARGET_BRAND = _env_dict.get("TARGET_BRAND") or os.getenv("TARGET_BRAND") or "FounderWing"
TARGET_BRAND_COLOR = _env_dict.get("TARGET_BRAND_COLOR") or os.getenv("TARGET_BRAND_COLOR") or "#E63946"
