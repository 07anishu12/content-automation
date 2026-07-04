import os
import sys
import traceback

def run_verification():
    print("=== STARTING INSTAGRAM PIPELINE VERIFICATION (STEP 3) ===")
    
    results = {}
    
    # 1. Verify Configuration loading
    try:
        from core.config import config
        print("✓ core.config imports successfully.")
        print(f"  TARGET_NICHE: {config.TARGET_NICHE}")
        print(f"  TARGET_BRAND: {config.TARGET_BRAND}")
        results["Configuration Load"] = "PASS"
    except Exception as e:
        print(f"❌ Configuration Load Failed: {e}")
        results["Configuration Load"] = f"FAIL: {e}"

    # 2. Verify Models import
    try:
        from core.models.models import ResearchItem, NewsArticle, ContentIdea, PublishJob, Asset
        print("✓ core.models imports successfully.")
        results["Models Verification"] = "PASS"
    except Exception as e:
        print(f"❌ Models Verification Failed: {e}")
        results["Models Verification"] = f"FAIL: {e}"

    # 3. Verify Research Engine
    try:
        from core.research.research_engine import ResearchEngine
        engine = ResearchEngine()
        subreddits = engine._get_subreddits()
        print(f"✓ Research Engine initialized. Mapped subreddits: {subreddits}")
        results["Research Engine"] = "PASS"
    except Exception as e:
        print(f"❌ Research Engine Failed: {e}")
        results["Research Engine"] = f"FAIL: {e}"

    # 4. Verify Topic Intelligence
    try:
        from core.research.topic_intelligence import TopicIntelligence
        intelligence = TopicIntelligence(niche="AI")
        print("✓ Topic Intelligence engine loaded.")
        results["Topic Intelligence"] = "PASS"
    except Exception as e:
        print(f"❌ Topic Intelligence Failed: {e}")
        results["Topic Intelligence"] = f"FAIL: {e}"

    # 5. Verify Content Engine
    try:
        from core.content.instagram_content_engine import InstagramContentEngine
        content_engine = InstagramContentEngine()
        fmt = content_engine.determine_format("Testing post title", "This is short context.")
        print(f"✓ Content Engine loaded. Formatting determined: {fmt}")
        results["Content Engine"] = "PASS"
    except Exception as e:
        print(f"❌ Content Engine Failed: {e}")
        results["Content Engine"] = f"FAIL: {e}"

    # 6. Verify Visuals Engine
    try:
        from core.visuals.visuals_engine import VisualsEngine
        visuals = VisualsEngine()
        print("✓ Visuals Engine loaded.")
        results["Visuals Engine"] = "PASS"
    except Exception as e:
        print(f"❌ Visuals Engine Failed: {e}")
        results["Visuals Engine"] = f"FAIL: {e}"

    # 7. Verify Publishing Publisher Adapter
    try:
        from adapters.instagram.publisher.instagram_publisher_adapter import InstagramPublisherAdapter
        publisher = InstagramPublisherAdapter()
        print("✓ Instagram Publisher Adapter loaded.")
        results["Publisher Adapter"] = "PASS"
    except Exception as e:
        print(f"❌ Publisher Adapter Failed: {e}")
        results["Publisher Adapter"] = f"FAIL: {e}"

    # 8. Check visual templates existence
    template_path = "./adapters/instagram/assets/instagram-carousel-template.html"
    if os.path.exists(template_path):
        print(f"✓ Instagram visual templates exist at: {template_path}")
        results["Templates Check"] = "PASS"
    else:
        print(f"❌ Template missing at: {template_path}")
        results["Templates Check"] = "FAIL: Missing Template"

    # Print Final Verification Summary
    print("\n=== VERIFICATION SUMMARY ===")
    all_passed = True
    for key, val in results.items():
        print(f"[{val}] {key}")
        if "FAIL" in val:
            all_passed = False
            
    if all_passed:
        print("\n🎉 ALL VERIFICATION CHECKS PASSED SUCCESSFULLY!")
        return True
    else:
        print("\n❌ SOME VERIFICATION CHECKS FAILED. PLEASE CORRECT THEM.")
        return False

if __name__ == "__main__":
    success = run_verification()
    sys.exit(0 if success else 1)
