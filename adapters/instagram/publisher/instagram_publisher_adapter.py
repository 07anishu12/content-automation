import os
import json
import datetime
from core.interfaces.interfaces import Publisher, Scheduler
from core.models.models import PublishJob
from send_to_slack import send_slack_message, upload_slack_file

class InstagramPublisherAdapter(Publisher, Scheduler):
    def __init__(self):
        self.history_path = "./scheduled_history.json"

    def publish_slack(self, job: PublishJob) -> bool:
        # Prepares a beautiful review format for the Slack channel
        slack_text = f"""
📢 *[INSTAGRAM CAMPAIGN REVIEW]*
*Post ID*: `{job.post_id}`
*Scheduled Time*: `{job.scheduled_time or 'Immediate'}`

*Caption Copy*:
{job.text_content}

*Visual Assets Attached*: {len(job.assets)} files.
"""
        try:
            print(f"Delivering Instagram preview card to Slack channel...")
            send_slack_message(slack_text)
            
            # If assets exist, upload them to Slack too
            for asset in job.assets:
                if os.path.exists(asset.file_path):
                    print(f"Uploading visual asset: {asset.file_name}...")
                    upload_slack_file(asset.file_path, asset.file_name, f"Asset for {job.post_id}")
            return True
        except Exception as e:
            print(f"Error publishing Instagram draft preview to Slack: {e}")
            return False

    def schedule_posts(self, jobs: list[PublishJob]) -> bool:
        history = []
        if os.path.exists(self.history_path):
            try:
                with open(self.history_path, "r", encoding="utf-8") as f:
                    history = json.load(f)
            except Exception:
                pass

        for job in jobs:
            job_dict = {
                "post_id": job.post_id,
                "status": "SCHEDULED",
                "caption": job.text_content,
                "assets": [
                    {
                        "file_path": asset.file_path,
                        "file_type": asset.file_type,
                        "file_name": asset.file_name
                    }
                    for asset in job.assets
                ],
                "scheduled_time": job.scheduled_time or datetime.datetime.now().isoformat(),
                "created_at": datetime.datetime.now().isoformat()
            }
            history.append(job_dict)
            print(f"Scheduled V2 post {job.post_id} at {job_dict['scheduled_time']}")

        try:
            with open(self.history_path, "w", encoding="utf-8") as f:
                json.dump(history, f, indent=2)
            return True
        except Exception as e:
            print(f"Error logging scheduled posts: {e}")
            return False
