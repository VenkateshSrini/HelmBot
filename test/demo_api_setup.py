"""
Demo script showing API key prompting behavior
"""
import os
import sys

# Add parent directory to Python path to access HelmBot modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def demo_api_key_setup():
    """Demonstrate API key setup for different providers"""
    print("🎯 HelmBot API Key Setup Demo")
    print("=" * 50)
    
    # Show current configuration
    from config import PROVIDER, DEFAULT_MODEL
    print(f"📋 Current Configuration:")
    print(f"   Provider: {PROVIDER}")
    print(f"   Model: {DEFAULT_MODEL}")
    
    # Check environment variables
    print(f"\n🔍 Environment Check:")
    openai_key_set = 'OPENAI_API_KEY' in os.environ and os.environ['OPENAI_API_KEY'].strip()
    anthropic_key_set = 'ANTHROPIC_API_KEY' in os.environ and os.environ['ANTHROPIC_API_KEY'].strip()
    
    print(f"   OpenAI API Key: {'✅ Set' if openai_key_set else '❌ Not Set'}")
    print(f"   Anthropic API Key: {'✅ Set' if anthropic_key_set else '❌ Not Set'}")
    
    # Show what will happen
    print(f"\n🤖 What happens when you run HelmBot:")
    
    if PROVIDER == 'anthropic' and not anthropic_key_set:
        print("   🔑 Will prompt for Anthropic API key")
        print("   💡 Get your key from: https://console.anthropic.com/")
    elif PROVIDER == 'openai' and not openai_key_set:
        print("   🔑 Will prompt for OpenAI API key")
        print("   💡 Get your key from: https://platform.openai.com/api-keys")
    else:
        print("   ✅ API key already configured, ready to go!")
    
    print(f"\n📝 To set API key manually:")
    if PROVIDER == 'anthropic':
        print("   Windows: set ANTHROPIC_API_KEY=your-key-here")
        print("   Linux/Mac: export ANTHROPIC_API_KEY=your-key-here")
    else:
        print("   Windows: set OPENAI_API_KEY=your-key-here")
        print("   Linux/Mac: export OPENAI_API_KEY=your-key-here")
    
    print(f"\n🔄 To switch providers:")
    print("   1. Edit config.py")
    print("   2. Change PROVIDER = 'openai' or 'anthropic'")
    print("   3. Update model names accordingly")
    
    print(f"\n✅ Demo complete!")

if __name__ == "__main__":
    demo_api_key_setup()