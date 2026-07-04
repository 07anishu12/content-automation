import os
import json
import datetime
from core.config import config

class InstagramPublisher:
    def __init__(self):
        self.history_path = os.path.join(config.ROOT_DIR, "scheduled_history.json")

    def create_draft(self, post_data: dict) -> dict:
        draft = {
            "post_id": f"draft_{int(datetime.datetime.now().timestamp())}",
            "status": "DRAFT",
            "format": post_data.get("format", "STATIC_POST"),
            "caption": post_data.get("post_text", ""),
            "hashtags": post_data.get("hashtags", []),
            "visual_assets": post_data.get("assets", []),
            "created_at": datetime.datetime.now().isoformat()
        }
        print(f"Created post draft: {draft['post_id']}")
        return draft

    def approve_draft(self, draft: dict) -> dict:
        draft["status"] = "APPROVED"
        draft["approved_at"] = datetime.datetime.now().isoformat()
        print(f"Draft {draft['post_id']} approved.")
        return draft

    def schedule_post(self, draft: dict, publish_time: str) -> dict:
        draft["status"] = "SCHEDULED"
        draft["scheduled_time"] = publish_time
        print(f"Scheduled post {draft['post_id']} for {publish_time}.")
        
        # Save to scheduled_history.json
        history = []
        if os.path.exists(self.history_path):
            try:
                with open(self.history_path, "r") as f:
                    history = json.load(f)
            except Exception:
                pass
        
        history.append(draft)
        with open(self.history_path, "w") as f:
            json.dump(history, f, indent=2)
            
        return draft

    def verify_publishing(self, post_id: str) -> bool:
        # Check in history if scheduled post exists and simulate verification
        if not os.path.exists(self.history_path):
            return False
            
        with open(self.history_path, "r") as f:
            history = json.load(f)
            
        for item in history:
            if item.get("post_id") == post_id:
                item["status"] = "PUBLISHED"
                item["published_at"] = datetime.datetime.now().isoformat()
                print(f"Verified and published post {post_id}.")
                
                with open(self.history_path, "w") as out:
                    json.dump(history, out, indent=2)
                return True
        return False
