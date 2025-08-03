"""Question generator and answer collector"""
import os
from langchain.prompts import PromptTemplate
from config import TEMPLATE_DIR, GENERATED_QUESTIONS_FILE


class QuestionManager:
    def __init__(self, llm_manager, helm_parser):
        self.llm_manager = llm_manager
        self.helm_parser = helm_parser
    
    def create_prompt_template(self):
        """Create prompt template for question generation"""
        prompt = PromptTemplate(
            input_variables=['variables'],
            template="""Given the following Helm chart variables: {variables}
                        Generate the minimum set of user-friendly questions needed to configure all these values.
                        Group related variables together where possible to minimize the number of questions.
                        Make the questions clear and understandable for users who may not be Kubernetes experts.
                        Format your response as a numbered list of questions.
                        For each question, briefly explain what the variable controls in parentheses.
                        Example format:
                        1. What is the name of your application? (Sets the app name used in labels and resources)
                        2. How many replicas do you want to run? (Controls horizontal scaling)
                        """
        )
        return prompt
    
    def ensure_questions_exist(self):
        """Check if questions exist, generate if not"""
        gen_q_path = os.path.join(TEMPLATE_DIR, GENERATED_QUESTIONS_FILE)
        if not os.path.exists(gen_q_path):
            print(f"❌ Question file '{gen_q_path}' does not exist. Hence generating the questions.")
            self._generate_questions()
        return gen_q_path
    
    def _generate_questions(self):
        """Internal method to generate questions"""
        files = self.helm_parser.list_template_files()
        variables = self.helm_parser.extract_variables(files)
        llm = self.llm_manager.get_gpt35_llm()
        prompt = self.create_prompt_template()
        self.generate_questions_for_variables(llm, prompt, variables)
    
    def generate_questions_for_variables(self, llm, prompt, variables_list):
        """Generate user-friendly questions for Helm chart variables"""
        if not variables_list:
            print("❌ No variables found to generate questions for.")
            return None
        formatted_prompt = prompt.format(variables=', '.join(sorted(variables_list)))
        response = llm.invoke(formatted_prompt)
        print("🎯 Generated Questions:")
        print(response.content)
        with open(os.path.join(TEMPLATE_DIR, GENERATED_QUESTIONS_FILE), 'w', encoding='utf-8') as file:
            file.write(response.content)
        print(f"\n💾 Questions saved to '{GENERATED_QUESTIONS_FILE}'")
        return response.content
    
    def collect_answers(self, questions_path):
        """Collect answers from user for generated questions"""
        if not os.path.exists(questions_path):
            print(f"❌ {questions_path} not found. Please run the previous steps to generate questions.")
            return None
        with open(questions_path, 'r', encoding='utf-8') as f:
            questions = [q.strip() for q in f.readlines() if q.strip()]
        print(f"✅ Loaded {len(questions)} questions from {GENERATED_QUESTIONS_FILE}\n")
        answers = []
        print("Please answer the following questions to generate your values.yaml:")
        for idx, question in enumerate(questions, 1):
            answer = input(f"\nQ{idx}: {question}\nYour answer: ")
            answers.append((question, answer))
        return answers
