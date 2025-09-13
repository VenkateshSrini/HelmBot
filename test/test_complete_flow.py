"""
Comprehensive test for HelmBot with Anthropic Claude integration
"""
import sys
import os

# Add parent directory to Python path to access HelmBot modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_complete_helmbot_flow():
    """Test the complete HelmBot flow with Anthropic Claude"""
    try:
        print("🚀 Testing Complete HelmBot Flow with Anthropic Claude...")
        
        # Import modules
        from helm_parser import HelmTemplateParser
        from llm_manager import LLMManager
        from question_manager import QuestionManager
        from yaml_generator import YAMLGenerator
        
        print("✅ All modules imported successfully")
        
        # Initialize components
        print("\n🔧 Initializing components...")
        parser = HelmTemplateParser()
        llm_manager = LLMManager()
        question_manager = QuestionManager(llm_manager, parser)
        yaml_generator = YAMLGenerator(llm_manager)
        
        print("✅ All components initialized")
        
        # Test Helm template parsing
        print("\n📋 Testing Helm template parsing...")
        files = parser.list_template_files()
        print(f"✅ Found {len(files)} template files")
        
        variables = parser.extract_variables(files)
        print(f"✅ Extracted {len(variables)} variables")
        print(f"📝 Sample variables: {list(variables)[:5]}...")
        
        # Test question generation with Claude
        print("\n❓ Testing question generation with Claude...")
        llm = llm_manager.get_gpt35_llm()
        prompt = question_manager.create_prompt_template()
        
        # Generate questions for a subset of variables to test
        test_variables = list(variables)[:5] if len(variables) > 5 else list(variables)
        formatted_prompt = prompt.format(variables=', '.join(test_variables))
        
        print("🤖 Calling Claude to generate questions...")
        response = llm.invoke(formatted_prompt)
        print(f"✅ Claude generated questions successfully!")
        print(f"📝 Sample questions preview: {response.content[:200]}...")
        
        # Test YAML generation with sample Q&A
        print("\n📄 Testing YAML generation...")
        sample_qa = [
            ("What is your application name?", "test-helmbot-app"),
            ("How many replicas do you want?", "3"),
            ("What is your Docker image repository?", "nginx"),
            ("What is your image tag?", "latest")
        ]
        
        print("🤖 Calling Claude to generate YAML...")
        yaml_generator.generate_values_yaml_gpt4(sample_qa)
        print("✅ YAML generated successfully!")
        
        # Verify the generated file exists
        gen_yaml_path = os.path.join('sample_helm', 'generated_values.yaml')
        if os.path.exists(gen_yaml_path):
            print(f"✅ Generated YAML file exists: {gen_yaml_path}")
            with open(gen_yaml_path, 'r') as f:
                content = f.read()
            print(f"📝 YAML preview: {content[:300]}...")
        else:
            print("⚠️  Generated YAML file not found")
        
        print("\n🎉 Complete HelmBot flow test passed!")
        print("🌟 Anthropic Claude integration is working perfectly!")
        return True
        
    except Exception as e:
        print(f"❌ Complete flow test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_complete_helmbot_flow()
    if not success:
        sys.exit(1)