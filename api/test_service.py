"""
Simple test to verify API functionality
"""
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from api.service import HelmBotService


def test_service():
    """Test the HelmBot service functionality"""
    print("🧪 Testing HelmBot Service...")
    
    try:
        # Initialize service
        service = HelmBotService()
        print("✅ Service initialized successfully")
        
        # Test getting questions
        print("\n📋 Testing question generation...")
        questions = service.get_questions()
        print(f"✅ Generated {len(questions)} questions")
        
        if questions:
            print("📝 Sample questions:")
            for i, q in enumerate(questions[:3], 1):
                print(f"  {i}. {q}")
        
        # Test YAML generation with sample answers
        print("\n🔧 Testing YAML generation...")
        sample_qa = [
            ("What is your application name?", "test-app"),
            ("How many replicas do you need?", "2")
        ]
        
        yaml_content, file_path = service.generate_yaml(sample_qa)
        print(f"✅ YAML generated successfully")
        print(f"📁 Saved to: {file_path}")
        print("\n--- Sample YAML Output ---")
        print(yaml_content[:300] + "..." if len(yaml_content) > 300 else yaml_content)
        
        print("\n🎉 All tests passed!")
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    test_service()
