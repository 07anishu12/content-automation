import os
import sys
import json
from core.config import config
from core.research.research_engine import ResearchEngine
from core.research.topic_intelligence import TopicIntelligence
from core.content.instagram_content_engine import InstagramContentEngine
from core.visuals.visuals_engine import VisualsEngine
from core.publishing.instagram_publisher import InstagramPublisher

def main():
    print(f"=== Starting Instagram Automation Pipeline (V2) ===")
    print(f"Niche: {config.TARGET_NICHE}")
    print(f"Brand: {config.TARGET_BRAND}")
    
    # 1. Fetching raw signal content
    research = ResearchEngine()
    print("Fetching raw data signals...")
    reddit_items = research.fetch_reddit_posts()
    news_items = research.fetch_news_articles()
    
    print(f"Fetched {len(reddit_items)} Reddit posts and {len(news_items)} RSS articles.")
    
    if not reddit_items and news_items:
        print("Reddit scraping was blocked/empty. Falling back to RSS news articles...")
        from core.models.models import ResearchItem
        for article in news_items:
            reddit_items.append(ResearchItem(
                subreddit=article.source,
                title=article.title,
                selftext=article.description,
                ups=100,
                num_comments=10,
                url=article.url,
                image_url=None
            ))
            
    if not reddit_items:
        print("Error: No research items found from Reddit or RSS. Exiting.")
        sys.exit(1)
        
    # 2. Topic Intelligence and scoring
    print("Scoring and ranking candidate topics...")
    intelligence = TopicIntelligence(niche=config.TARGET_NICHE)
    ranked_topics = intelligence.rank_topics(reddit_items, limit=5)
    
    for idx, rt in enumerate(ranked_topics):
        print(f"Rank {idx+1}: Score: {rt['score']} | {rt['item'].title}")
        
    winner = ranked_topics[0]["item"]
    print(f"\nWinning Topic: {winner.title}")
    
    # 3. Instagram Content generation
    print("Generating post, caption and design configurations...")
    content_engine = InstagramContentEngine()
    post_payload = content_engine.generate_content(winner.title, winner.selftext)
    
    print("Post copy preview:")
    print(post_payload.get("post_text")[:200] + "...")
    
    # Save post texts to disk
    with open("./instagram_post_output.json", "w") as f:
        json.dump(post_payload, f, indent=2)
        
    # 4. Visual compilations
    print("Building visual layouts...")
    visuals = VisualsEngine()
    
    if post_payload.get("format") == "CAROUSEL" and post_payload.get("carousel_slides"):
        visuals.build_carousel_slides(post_payload["carousel_slides"])
    elif post_payload.get("format") == "INFOGRAPHIC" and post_payload.get("infographic_data"):
        visuals.write_infographic_html(post_payload["infographic_data"])
    else:
        print("Static Post layout setup completed.")
        
    # Compile assets if Puppeteer exists and trigger scripts
    visuals.compile_assets()
    
    # 5. Publishing draft
    publisher = InstagramPublisher()
    draft = publisher.create_draft(post_payload)
    approved = publisher.approve_draft(draft)
    scheduled = publisher.schedule_post(approved, "2026-07-05T10:00:00")
    
    print(f"\n=== Campaign generation completed successfully! Post ID: {scheduled['post_id']} ===")

if __name__ == "__main__":
    main()
