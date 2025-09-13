"""
Test script to verify LLM manager works with Anthropic Claude
"""
import sys
import os

# Add parent directory to Python path to access HelmBot modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_llm_manager():
    """Test the LLM manager with Anthropic Claude"""
    try:
        print("🧪 Testing LLM Manager with Anthropic Claude...")
        
        # Import and initialize
        from llm_manager import LLMManager
        from config import PROVIDER, DEFAULT_MODEL, GPT4_MODEL
        
        print(f"📋 Current provider: {PROVIDER}")
        print(f"📋 Default model: {DEFAULT_MODEL}")
        print(f"📋 Advanced model: {GPT4_MODEL}")
        
        # Initialize LLM manager
        llm_manager = LLMManager()
        
        # Get provider info
        provider_info = llm_manager.get_provider_info()
        print(f"✅ Provider info: {provider_info}")
        
        # Test getting LLM instances
        print("\n🔧 Testing LLM instance creation...")
        
        # Test default model
        llm_default = llm_manager.get_gpt35_llm()
        print(f"✅ Default model LLM created: {type(llm_default).__name__}")
        
        # Test advanced model
        llm_advanced = llm_manager.get_gpt4_llm()
        print(f"✅ Advanced model LLM created: {type(llm_advanced).__name__}")
        
        # Test a simple prompt
        print("\n💬 Testing simple prompt...")
        test_prompt = "Say 'Hello from Claude!' in exactly 3 words."
        response = llm_default.invoke(test_prompt)
        print(f"✅ Claude response: {response.content}")
        
        print("\n🎉 All LLM manager tests passed!")
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_llm_manager()
    if not success:
        sys.exit(1)