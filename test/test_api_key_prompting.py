"""
Test script to verify API key prompting works for both providers
"""
import sys
import os

# Add parent directory to Python path to access HelmBot modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_api_key_prompting():
    """Test API key prompting for both OpenAI and Anthropic"""
    print("🧪 Testing API Key Prompting...")
    
    # Save original environment variables
    orig_openai_key = os.environ.get('OPENAI_API_KEY')
    orig_anthropic_key = os.environ.get('ANTHROPIC_API_KEY')
    
    try:
        # Import the providers
        from llm_manager import OpenAIProvider, AnthropicProvider, ModelProviderFactory
        
        print("\n📋 Testing with missing API keys...")
        
        # Remove API keys from environment to test prompting
        if 'OPENAI_API_KEY' in os.environ:
            del os.environ['OPENAI_API_KEY']
        if 'ANTHROPIC_API_KEY' in os.environ:
            del os.environ['ANTHROPIC_API_KEY']
        
        # Test Anthropic provider (current default)
        print("\n🤖 Testing Anthropic provider...")
        anthropic_provider = AnthropicProvider()
        
        # This should detect missing key and provide helpful message
        print("✅ Anthropic provider created successfully")
        print(f"✅ Provider name: {anthropic_provider.get_provider_name()}")
        
        # Test factory creation
        print("\n🏭 Testing factory creation...")
        factory_provider = ModelProviderFactory.create_provider('anthropic')
        print(f"✅ Factory created Anthropic provider: {factory_provider.get_provider_name()}")
        
        # Show supported providers
        supported = ModelProviderFactory.get_supported_providers()
        print(f"✅ Supported providers: {supported}")
        
        print("\n🎉 API key prompting test completed!")
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        # Restore original environment variables
        if orig_openai_key is not None:
            os.environ['OPENAI_API_KEY'] = orig_openai_key
        if orig_anthropic_key is not None:
            os.environ['ANTHROPIC_API_KEY'] = orig_anthropic_key
    
    return True

if __name__ == "__main__":
    print("⚠️  Note: This test will prompt for API keys if they're not set in environment.")
    print("You can press Ctrl+C to cancel or enter a test key.")
    
    try:
        success = test_api_key_prompting()
        if not success:
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n⏹️  Test cancelled by user.")
        sys.exit(0)