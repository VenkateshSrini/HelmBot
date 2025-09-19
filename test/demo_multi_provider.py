"""
Example script demonstrating all three AI providers: OpenAI, Anthropic, and AWS Bedrock
"""
import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from llm_manager import ModelProviderFactory, LLMManager
import config

def demonstrate_provider(provider_name, model_name):
    """Demonstrate functionality of a specific provider"""
    print(f"\n🔄 Testing {provider_name.upper()} Provider")
    print("=" * 50)
    
    try:
        # Temporarily switch configuration
        original_provider = config.PROVIDER
        original_model = config.DEFAULT_MODEL
        
        config.PROVIDER = provider_name
        config.DEFAULT_MODEL = model_name
        
        # Create provider instance
        provider = ModelProviderFactory.create_provider(provider_name)
        print(f"✅ Created {provider.get_provider_name()} provider")
        
        # Setup credentials (will prompt if needed)
        provider.setup_api_key()
        
        # Create LLM Manager
        llm_manager = LLMManager()
        
        # Get provider info
        info = llm_manager.get_provider_info()
        print(f"📊 Provider Info: {info}")
        
        # Test simple query
        print(f"🧪 Testing with a simple query...")
        llm = llm_manager.get_llm()
        
        test_prompt = f"Please respond with exactly: '{provider_name.upper()} is working correctly!'"
        response = llm.invoke(test_prompt)
        print(f"🤖 Response: {response.content}")
        
        # Restore configuration
        config.PROVIDER = original_provider
        config.DEFAULT_MODEL = original_model
        
        print(f"✅ {provider_name.upper()} provider test completed successfully!")
        return True
        
    except Exception as e:
        print(f"❌ {provider_name.upper()} provider test failed: {e}")
        return False

def main():
    """Main demonstration function"""
    print("🚀 HelmBot Multi-Provider Demonstration")
    print("=" * 60)
    print("This script will demonstrate all three supported AI providers:")
    print("1. Anthropic Claude (currently active)")
    print("2. OpenAI GPT")
    print("3. AWS Bedrock")
    print("\nNote: You'll need API keys/credentials for each provider you want to test.")
    
    # Available providers with their recommended models
    providers = {
        'anthropic': 'claude-sonnet-4-20250514',
        'openai': 'gpt-3.5-turbo',
        'bedrock': 'anthropic.claude-3-5-sonnet-20241022-v2:0'
    }
    
    results = {}
    
    for provider, model in providers.items():
        print(f"\n" + "="*60)
        user_input = input(f"🤔 Test {provider.upper()} provider? (y/n): ").strip().lower()
        
        if user_input in ['y', 'yes']:
            results[provider] = demonstrate_provider(provider, model)
        else:
            print(f"⏭️  Skipping {provider.upper()} provider")
            results[provider] = None
    
    # Summary
    print(f"\n" + "="*60)
    print("📊 TESTING SUMMARY")
    print("="*60)
    
    for provider, result in results.items():
        if result is True:
            print(f"✅ {provider.upper()}: PASSED")
        elif result is False:
            print(f"❌ {provider.upper()}: FAILED")
        else:
            print(f"⏭️  {provider.upper()}: SKIPPED")
    
    print(f"\n🎉 Multi-provider demonstration completed!")
    print(f"💡 You can switch providers by updating PROVIDER in config.py")

if __name__ == "__main__":
    main()