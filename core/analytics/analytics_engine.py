import os
import json
import datetime
from core.config import config

class AnalyticsEngine:
    def __init__(self):
        self.analytics_path = os.path.join(config.ROOT_DIR, "analytics_history.json")

    def track_metrics(self, post_id: str, metrics: dict) -> bool:
        # Load existing data
        history = {}
        if os.path.exists(self.analytics_path):
            try:
                with open(self.analytics_path, "r") as f:
                    history = json.load(f)
            except Exception:
                pass

        # Update metrics for post
        history[post_id] = {
            "reach": metrics.get("reach", 0),
            "impressions": metrics.get("impressions", 0),
            "likes": metrics.get("likes", 0),
            "shares": metrics.get("shares", 0),
            "saves": metrics.get("saves", 0),
            "comments": metrics.get("comments", 0),
            "profile_visits": metrics.get("profile_visits", 0),
            "link_clicks": metrics.get("link_clicks", 0),
            "follower_growth": metrics.get("follower_growth", 0),
            "tracked_at": datetime.datetime.now().isoformat()
        }

        try:
            with open(self.analytics_path, "w") as f:
                json.dump(history, f, indent=2)
            print(f"Logged analytics for post {post_id}: Reach: {metrics.get('reach')}, Likes: {metrics.get('likes')}")
            return True
        except Exception as e:
            print(f"Error saving analytics: {e}")
            return False

    def get_aggregate_stats(self) -> dict:
        if not os.path.exists(self.analytics_path):
            return {}

        with open(self.analytics_path, "r") as f:
            data = json.load(f)

        totals = {
            "reach": 0,
            "impressions": 0,
            "likes": 0,
            "shares": 0,
            "saves": 0,
            "comments": 0,
            "profile_visits": 0,
            "link_clicks": 0,
            "follower_growth": 0
        }

        for post_id, metrics in data.items():
            for key in totals:
                totals[key] += metrics.get(key, 0)

        return totals
