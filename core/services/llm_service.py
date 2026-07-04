import json
import urllib.request
import ssl
import time
import traceback
from core.config import config

class LLMService:
    def __init__(self):
        self.ctx = ssl.create_default_context()
        self.ctx.check_hostname = False
        self.ctx.verify_mode = ssl.CERT_NONE
        self.openrouter_key = config.OPENROUTER_API_KEY
        self.url = config.OPENROUTER_URL
        self.headers = {
            "Authorization": f"Bearer {self.openrouter_key}",
            "Content-Type": "application/json"
        }

    def call_gemini(self, system_prompt, prompt, max_tokens=4000, model=None):
        target_model = model or config.OPENROUTER_MODEL
        payload = {
            "model": target_model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            "max_tokens": max_tokens
        }
        
        req = urllib.request.Request(
            self.url,
            data=json.dumps(payload).encode("utf-8"),
            headers=self.headers,
            method="POST"
        )
        
        for attempt in range(5):
            try:
                with urllib.request.urlopen(req, context=self.ctx) as res:
                    resp = json.loads(res.read().decode("utf-8"))
                    if resp and "choices" in resp and len(resp["choices"]) > 0:
                        return resp["choices"][0]["message"]["content"]
                    else:
                        print(f"OpenRouter returned unexpected response format: {resp}")
            except urllib.error.HTTPError as e:
                if e.code == 429:
                    print(f"Rate limited (429) on OpenRouter. Retrying in {10 * (attempt + 1)}s...")
                    time.sleep(10 * (attempt + 1))
                else:
                    print(f"HTTP Error calling OpenRouter: {e.code} - {e.reason}")
                    try:
                        print("Error body:", e.read().decode("utf-8"))
                    except:
                        pass
                    break
            except Exception as e:
                traceback.print_exc()
                print(f"Error calling OpenRouter: {e}")
                break
            time.sleep(2)
        return None
