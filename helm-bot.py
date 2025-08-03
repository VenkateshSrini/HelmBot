"""
Helm Bot - Main application entry point
Dependencies: pip install langchain langchain_community openai
"""
import os
from config import TEMPLATE_DIR, GENERATED_QUESTIONS_FILE
from helm_parser import HelmTemplateParser
from llm_manager import LLMManager
from question_manager import QuestionManager
from yaml_generator import YAMLGenerator

def main():
    """Main application flow"""
    # Initialize components
    parser = HelmTemplateParser()
    llm_manager = LLMManager()
    question_manager = QuestionManager(llm_manager, parser)
    yaml_generator = YAMLGenerator(llm_manager)
    
    # Ensure questions exist (will generate if missing)
    gen_q_path = question_manager.ensure_questions_exist()
    
    # Collect answers and generate YAML
    answers = question_manager.collect_answers(gen_q_path)
    if answers:
        yaml_generator.generate_values_yaml_gpt4(answers)

if __name__ == "__main__":
    main()
