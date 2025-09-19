"""Test script for AWS Bedrock LLM functionality"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_bedrock_llm():
    """Test AWS Bedrock LLM functionality"""
    print("🧪 Testing AWS Bedrock LLM functionality...")
    
    try:
        # Temporarily switch to Bedrock in config
        import config
        original_provider = config.PROVIDER
        original_model = config.DEFAULT_MODEL
        
        # Set Bedrock configuration
        config.PROVIDER = 'bedrock'
        config.DEFAULT_MODEL = 'anthropic.claude-3-5-sonnet-20241022-v2:0'
        
        from llm_manager import LLMManager
        
        # Initialize LLM Manager with Bedrock
        llm_manager = LLMManager()
        
        # Test basic LLM creation
        llm = llm_manager.get_llm()
        print(f"✅ Successfully created Bedrock LLM instance")
        
        # Test a simple query
        test_prompt = "Hello! Please respond with just 'AWS Bedrock is working!' to confirm the connection."
        print(f"🔄 Testing with prompt: {test_prompt}")
        
        response = llm.invoke(test_prompt)
        print(f"✅ Bedrock Response: {response.content}")
        
        # Test provider info
        provider_info = llm_manager.get_provider_info()
        print(f"📊 Provider Info: {provider_info}")
        
        # Restore original configuration
        config.PROVIDER = original_provider
        config.DEFAULT_MODEL = original_model
        
        print("🎉 AWS Bedrock test completed successfully!")
        return True
        
    except ImportError as e:
        print(f"❌ Import Error: {e}")
        print("💡 Make sure to install: pip install langchain-aws boto3")
        return False
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        print("💡 Make sure your AWS credentials are configured correctly")
        return False

def test_all_providers():
    """Test all available providers"""
    print("🧪 Testing all LLM providers...")
    
    from llm_manager import ModelProviderFactory
    
    providers = ModelProviderFactory.get_supported_providers()
    print(f"📋 Available providers: {providers}")
    
    for provider in providers:
        print(f"\n--- Testing {provider.upper()} Provider ---")
        try:
            provider_instance = ModelProviderFactory.create_provider(provider)
            print(f"✅ Successfully created {provider_instance.get_provider_name()} provider")
        except Exception as e:
            print(f"❌ Failed to create {provider} provider: {e}")

if __name__ == "__main__":
    print("🚀 Starting AWS Bedrock Tests...")
    print("=" * 50)
    
    # Test provider factory
    test_all_providers()
    
    print("\n" + "=" * 50)
    
    # Test Bedrock specifically (only if user wants to)
    user_input = input("\n🤔 Do you want to test AWS Bedrock connection? (y/n): ").strip().lower()
    if user_input in ['y', 'yes']:
        test_bedrock_llm()
    else:
        print("⏭️  Skipping Bedrock connection test")
    
    print("\n✅ All tests completed!")