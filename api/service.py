"""
HelmBot service layer - Business logic for API endpoints
"""
import os
import sys
from typing import List, Tuple

# Add parent directory to path to import HelmBot modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import TEMPLATE_DIR, GENERATED_QUESTIONS_FILE
from helm_parser import HelmTemplateParser
from llm_manager import LLMManager
from question_manager import QuestionManager
from yaml_generator import YAMLGenerator


class HelmBotService:
    """Service class containing business logic for HelmBot API"""
    
    def __init__(self):
        """Initialize HelmBot components"""
        self.parser = HelmTemplateParser()
        self.llm_manager = LLMManager()
        self.question_manager = QuestionManager(self.llm_manager, self.parser)
        self.yaml_generator = YAMLGenerator(self.llm_manager)
    
    def get_questions(self) -> List[str]:
        """
        Get list of questions for Helm chart configuration
        
        Returns:
            List[str]: List of questions
        """
        try:
            # Ensure questions exist (will generate if missing)
            gen_q_path = self.question_manager.ensure_questions_exist()
            
            # Read questions from file
            with open(gen_q_path, 'r', encoding='utf-8') as f:
                questions = [q.strip() for q in f.readlines() if q.strip()]
            
            return questions
        except Exception as e:
            raise Exception(f"Failed to get questions: {str(e)}")
    
    def generate_yaml(self, qa_pairs: List[Tuple[str, str]]) -> Tuple[str, str]:
        """
        Generate YAML from question-answer pairs
        
        Args:
            qa_pairs: List of (question, answer) tuples
            
        Returns:
            Tuple[str, str]: (yaml_content, file_path)
        """
        try:
            if not qa_pairs:
                raise ValueError("No question-answer pairs provided")
            
            # Generate YAML using the existing yaml_generator
            self.yaml_generator.generate_values_yaml_gpt4(qa_pairs)
            
            # Read the generated YAML content
            generated_path = os.path.join(TEMPLATE_DIR, "generated_values.yaml")
            with open(generated_path, 'r', encoding='utf-8') as f:
                yaml_content = f.read()
            
            return yaml_content, generated_path
        except Exception as e:
            raise Exception(f"Failed to generate YAML: {str(e)}")
