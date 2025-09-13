"""
Quick verification test for Claude Sonnet 4 configuration
"""
import sys
import os

# Add parent directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def verify_claude_sonnet_4():
    """Verify Claude Sonnet 4 is properly configured"""
    try:
        # Import and check configuration
        from config import DEFAULT_MODEL, GPT4_MODEL, PROVIDER
        print(f"🔍 Configuration Check:")
        print(f"   Provider: {PROVIDER}")
        print(f"   Default Model: {DEFAULT_MODEL}")
        print(f"   Advanced Model: {GPT4_MODEL}")
        
        # Verify it's Claude Sonnet 4
        if 'claude-sonnet-4' in DEFAULT_MODEL:
            print("✅ Claude Sonnet 4 is correctly configured!")
        else:
            print("❌ Model is not Claude Sonnet 4")
            return False
        
        # Test LLM Manager initialization
        from llm_manager import LLMManager
        print("\n🧪 Testing LLM Manager...")
        llm_manager = LLMManager()
        print("✅ LLM Manager initialized successfully")
        
        # Get provider info
        provider_info = llm_manager.get_provider_info()
        print(f"✅ Provider Info: {provider_info}")
        
        # Test LLM instance creation (without actual API call)
        print("\n🔧 Testing LLM instance creation...")
        llm_instance = llm_manager.get_gpt35_llm()
        print(f"✅ LLM instance created: {type(llm_instance).__name__}")
        
        print("\n🎉 Claude Sonnet 4 verification completed successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Verification failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = verify_claude_sonnet_4()
    if not success:
        sys.exit(1)