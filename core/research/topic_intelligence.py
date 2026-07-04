import re
from typing import List, Dict
from core.models.models import ResearchItem

class TopicIntelligence:
    def __init__(self, niche: str, weights: Dict[str, float] = None):
        self.niche = niche
        # Defaults weights adding up to 1.0
        self.weights = weights or {
            "relevance": 0.25,
            "trend_strength": 0.25,
            "educational_value": 0.15,
            "engagement_potential": 0.15,
            "business_value": 0.20
        }
        
        # Business intent keywords mapping
        self.business_keywords = ["tool", "strategy", "startup", "revenue", "mrr", "money", "investing", "earn", "scale", "hack", "save", "roi", "product", "growth", "founder"]

    def calculate_score(self, item: ResearchItem) -> float:
        score_details = {}
        
        # 1. Relevance: checking matching keywords in title or body
        niche_words = re.findall(r"\w+", self.niche.lower())
        title_lower = item.title.lower()
        body_lower = item.selftext.lower()
        matches = sum(1 for word in niche_words if word in title_lower or word in body_lower)
        score_details["relevance"] = min(1.0, matches / max(1, len(niche_words)))
        
        # 2. Trend Strength: logarithmic scale of upvotes
        # Log scale mapping: 0 ups = 0.0, 100 ups = 0.5, 1000+ ups = 1.0
        import math
        ups_val = max(0, item.ups)
        score_details["trend_strength"] = min(1.0, math.log(ups_val + 1, 10) / 3.0)
        
        # 3. Educational Value: checking length of selftext
        # Max score at 500+ characters of content
        body_len = len(item.selftext)
        score_details["educational_value"] = min(1.0, body_len / 500.0)
        
        # 4. Engagement Potential: comment ratio
        # Mapping: high comment-to-upvote ratio indicates controversial or hot debate topics
        if ups_val > 0:
            ratio = item.num_comments / ups_val
            score_details["engagement_potential"] = min(1.0, ratio * 2.0)
        else:
            score_details["engagement_potential"] = min(1.0, item.num_comments / 10.0)
            
        # 5. Business Value: matching domain intent keywords
        business_matches = sum(1 for kw in self.business_keywords if kw in title_lower or kw in body_lower)
        score_details["business_value"] = min(1.0, business_matches / 3.0)
        
        # Calculate final weighted score
        final_score = sum(score_details[k] * self.weights[k] for k in self.weights)
        return round(final_score, 3)

    def rank_topics(self, items: List[ResearchItem], limit: int = 5) -> List[Dict]:
        ranked_list = []
        for item in items:
            score = self.calculate_score(item)
            ranked_list.append({
                "item": item,
                "score": score
            })
            
        # Sort desc by score
        ranked_list.sort(key=lambda x: x["score"], reverse=True)
        return ranked_list[:limit]
