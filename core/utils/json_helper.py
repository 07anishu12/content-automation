import json

class JsonHelper:
    @staticmethod
    def parse_llm_json(raw_text):
        if not raw_text:
            return {}
        text = raw_text.strip()
        if text.startswith("```json"):
            text = text[7:]
        elif text.startswith("```"):
            text = text[3:]
        if text.endswith("```"):
            text = text[:-3]
        text = text.strip()
        try:
            return json.loads(text)
        except Exception as e:
            print(f"Error parsing JSON: {e}")
            print("Raw text chunk was:", text)
            return {}
