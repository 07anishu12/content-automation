import os
import json
import urllib.request
import urllib.parse
import ssl
import xml.etree.ElementTree as ET
import html
import re
from typing import List
from core.config import config
from core.models.models import ResearchItem, NewsArticle
from core.interfaces.interfaces import ResearchProvider

class ResearchEngine(ResearchProvider):
    def __init__(self, niche: str = None):
        self.niche = niche or config.TARGET_NICHE
        self.ctx = ssl.create_default_context()
        self.ctx.check_hostname = False
        self.ctx.verify_mode = ssl.CERT_NONE
        
        # Mappings of niches to target subreddits
        self.niche_subreddits = {
            "Artificial Intelligence": ["artificial", "ChatGPT", "singularity", "OpenAI", "technology"],
            "Finance": ["personalfinance", "investing", "stocks", "financialindependence"],
            "Fitness": ["fitness", "bodybuilding", "nutrition", "gainit"],
            "SaaS": ["saas", "startups", "SideProject", "entrepreneur"],
            "Marketing": ["marketing", "socialmedia", "SEO"],
            "Travel": ["travel", "solotravel", "backpacking"]
        }
        
        # Mappings of niches to RSS news feeds
        self.niche_rss = {
            "Artificial Intelligence": [
                {"source": "TechCrunch AI", "url": "https://techcrunch.com/category/artificial-intelligence/feed/"},
                {"source": "VentureBeat AI", "url": "https://venturebeat.com/category/ai/feed/"}
            ],
            "Finance": [
                {"source": "Yahoo Finance", "url": "https://finance.yahoo.com/news/rssindex/"},
                {"source": "MarketWatch", "url": "https://feeds.brg.com/marketwatch/feeds/finance/"}
            ],
            "Technology": [
                {"source": "TechCrunch Tech", "url": "https://techcrunch.com/feed/"}
            ]
        }

    def _get_subreddits(self) -> List[str]:
        # Return mapped subreddits or generic fallback based on niche name
        for k, v in self.niche_subreddits.items():
            if k.lower() in self.niche.lower() or self.niche.lower() in k.lower():
                return v
        # Fallback to single subreddit matching niche name formatted
        clean_niche = "".join(c for c in self.niche if c.isalnum())
        return [clean_niche] if clean_niche else ["news"]

    def _get_rss_feeds(self) -> List[dict]:
        for k, v in self.niche_rss.items():
            if k.lower() in self.niche.lower() or self.niche.lower() in k.lower():
                return v
        # Fallback feed
        return [{"source": "TechCrunch", "url": "https://techcrunch.com/feed/"}]

    def fetch_reddit_posts(self) -> List[ResearchItem]:
        subreddits = self._get_subreddits()
        apify_token = config.APIFY_API_KEY
        normalized_posts = []

        if apify_token:
            # Trigger Apify Reddit Scraper Lite
            urls_payload = [{"url": f"https://www.reddit.com/r/{sub}/top/?t=week"} for sub in subreddits]
            payload = {
                "startUrls": urls_payload,
                "maxItems": 40
            }
            trigger_url = f"https://api.apify.com/v2/acts/trudax~reddit-scraper-lite/runs?token={apify_token}"
            req = urllib.request.Request(
                trigger_url,
                data=json.dumps(payload).encode("utf-8"),
                headers={"Content-Type": "application/json"},
                method="POST"
            )
            try:
                print(f"Triggering Apify Reddit scraper for subreddits: {subreddits}...")
                with urllib.request.urlopen(req, context=self.ctx) as res:
                    resp = json.loads(res.read().decode("utf-8"))
                    dataset_id = resp["data"]["defaultDatasetId"]
                    run_id = resp["data"]["id"]
                
                # Poll status
                status_url = f"https://api.apify.com/v2/actor-runs/{run_id}?token={apify_token}"
                import time
                for _ in range(30):
                    req_status = urllib.request.Request(status_url)
                    with urllib.request.urlopen(req_status, context=self.ctx) as status_res:
                        run_status = json.loads(status_res.read().decode("utf-8"))["data"]["status"]
                        if run_status in ["SUCCEEDED", "FAILED", "TIMED-OUT", "ABORTED"]:
                            break
                    time.sleep(5)
                
                if run_status == "SUCCEEDED":
                    items_url = f"https://api.apify.com/v2/datasets/{dataset_id}/items?token={apify_token}&limit=60"
                    req_items = urllib.request.Request(items_url)
                    with urllib.request.urlopen(req_items, context=self.ctx) as items_res:
                        items = json.loads(items_res.read().decode("utf-8"))
                        for item in items:
                            if item.get("dataType") == "comment" or not item.get("title"):
                                continue
                            
                            image_url = item.get("image_url")
                            if not image_url and item.get("url") and any(ext in item["url"].lower() for ext in [".png", ".jpg", ".jpeg", ".webp"]):
                                image_url = item["url"]
                            
                            normalized_posts.append(ResearchItem(
                                subreddit=item.get("communityName") or item.get("subreddit") or "r/niche",
                                title=item["title"],
                                selftext=item.get("body") or item.get("selftext") or "",
                                ups=item.get("score") or item.get("ups") or 0,
                                num_comments=item.get("num_comments") or 0,
                                url=item.get("url") or item.get("permalink") or "",
                                image_url=image_url
                            ))
            except Exception as e:
                print(f"Apify call failed: {e}. Falling back to direct JSON feeds.")
        
        # Fallback to direct Reddit JSON scraping if Apify fails or has no credentials
        if not normalized_posts:
            headers = {"User-Agent": "Mozilla/5.0"}
            for sub in subreddits[:3]:
                url = f"https://www.reddit.com/r/{sub}/top.json?limit=15&t=week&raw_json=1"
                req = urllib.request.Request(url, headers=headers)
                try:
                    with urllib.request.urlopen(req, context=self.ctx) as res:
                        data = json.loads(res.read().decode("utf-8"))
                        children = data.get("data", {}).get("children", [])
                        for child in children:
                            post_data = child.get("data", {})
                            if not post_data.get("title"):
                                continue
                            normalized_posts.append(ResearchItem(
                                subreddit=f"r/{sub}",
                                title=post_data["title"],
                                selftext=post_data.get("selftext") or "",
                                ups=post_data.get("ups") or 0,
                                num_comments=post_data.get("num_comments") or 0,
                                url=post_data.get("url") or "",
                                image_url=post_data.get("thumbnail") if post_data.get("thumbnail", "").startswith("http") else None
                            ))
                except Exception as e:
                    print(f"Error fetching JSON fallback for r/{sub}: {e}")

        return normalized_posts

    def fetch_news_articles(self) -> List[NewsArticle]:
        feeds = self._get_rss_feeds()
        articles = []
        headers = {"User-Agent": "Mozilla/5.0"}

        for feed in feeds:
            req = urllib.request.Request(feed["url"], headers=headers)
            try:
                with urllib.request.urlopen(req, context=self.ctx) as res:
                    root = ET.fromstring(res.read())
                    items = root.findall('.//item')
                    for item in items:
                        title_el = item.find('title')
                        title = title_el.text if title_el is not None else ""
                        
                        link_el = item.find('link')
                        link = link_el.text if link_el is not None else ""
                        
                        desc_el = item.find('description')
                        desc_html = desc_el.text if desc_el is not None else ""
                        
                        pub_el = item.find('pubDate')
                        pub_date = pub_el.text if pub_el is not None else ""
                        
                        clean_desc = ""
                        if desc_html:
                            decoded = html.unescape(desc_html)
                            text_with_newlines = re.sub(r'<(?:p|br|div)[^>]*>', '\n', decoded)
                            clean_desc = re.sub(r'<[^>]+>', '', text_with_newlines)
                            clean_desc = re.sub(r'\s+', ' ', clean_desc).strip()
                            
                        if title:
                            articles.append(NewsArticle(
                                source=feed["source"],
                                title=title,
                                description=clean_desc,
                                pubDate=pub_date,
                                url=link
                            ))
            except Exception as e:
                print(f"Error fetching news RSS feed {feed['source']}: {e}")
        return articles
