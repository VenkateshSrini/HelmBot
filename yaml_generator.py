"""YAML generator for creating values.yaml files"""
import os
from config import TEMPLATE_DIR, VALUES_FILE, GENERATED_VALUES_FILE


class YAMLGenerator:
    def __init__(self, llm_manager):
        self.llm_manager = llm_manager
    
    def generate_values_yaml_gpt4(self, answers):
        """Generate merged values.yaml using GPT-4.1"""
        llm_gpt4 = self.llm_manager.get_gpt4_llm()
        
        # Load base values.yaml
        values_path = os.path.join(TEMPLATE_DIR, VALUES_FILE)
        base_yaml_content = ''
        if os.path.exists(values_path):
            with open(values_path, 'r', encoding='utf-8') as f:
                base_yaml_content = f.read()
        else:
            print(f"Warning: {values_path} not found. Proceeding with user answers only.")
        
        qa_pairs = "\n".join([f"Q: {q}\nA: {a}" for q, a in answers])
        prompt_yaml = f"""
                        Given the following Helm chart configuration questions and user answers, and the existing values.yaml content below, replace the user answers into the values.yaml in appropriate places. Do not copy any old values from the existing values.yaml file.
                        Output only the final merged YAML, suitable for use as values.yaml. Do not include any explanation or extra text.

                        Existing values.yaml:
                        {base_yaml_content}

                        Questions and Answers:
                        {qa_pairs}
                        Example 1:
                        assuming the user image as mypp and tag as v1.0 and number of instances as 2, the output should look like:
                        replicaCount: 2
                        image:
                            repository: myapp
                            tag: v1.0
                            pullPolicy: IfNotPresent
                        """
        print("\n🚀 Sending values.yaml and user answers to GPT-4.1 to generate merged YAML...")
        response = llm_gpt4.invoke(prompt_yaml)
        merged_yaml = response.content.strip()
        
        generated_path = os.path.join(TEMPLATE_DIR, GENERATED_VALUES_FILE)
        with open(generated_path, 'w', encoding='utf-8') as f:
            f.write(merged_yaml)
        print(f"\n💾 Final merged values saved to {generated_path}\n")
        print("--- generated_values.yaml preview ---\n")
        print(merged_yaml)
        return merged_yaml
