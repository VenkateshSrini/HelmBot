"""
Simple API functionality test for Claude Sonnet 4
"""
import sys
import os

# Add parent directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_api_functionality():
    """Test that API functionality works with Claude Sonnet 4"""
    try:
        # Test API service import
        from api.service import HelmBotService
        print("✅ API Service imported successfully")
        
        # Test service initialization (will prompt for API key if needed)
        print("🔧 Initializing HelmBot Service...")
        service = HelmBotService()
        print("✅ HelmBot Service initialized")
        
        # Test question generation capability
        print("📋 Testing question generation capability...")
        questions = service.get_questions()
        print(f"✅ Generated {len(questions)} questions")
        
        if questions:
            print("📝 Sample questions:")
            for i, q in enumerate(questions[:3], 1):
                print(f"  {i}. {q[:60]}...")
        
        print("\n🎉 API functionality test completed successfully!")
        return True
        
    except Exception as e:
        print(f"❌ API test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_api_functionality()
    if not success:
        sys.exit(1)