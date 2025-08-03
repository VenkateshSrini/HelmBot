"""Configuration settings for Helm Bot"""
import os

# Directory paths
TEMPLATE_DIR = 'sample_helm'
TEMPLATES_SUBDIR = os.path.join(TEMPLATE_DIR, 'templates')

# File names
GENERATED_QUESTIONS_FILE = 'generated_questions.txt'
VALUES_FILE = 'values.yaml'
GENERATED_VALUES_FILE = 'generated_values.yaml'

# LLM settings
DEFAULT_MODEL = 'gpt-3.5-turbo'
GPT4_MODEL = 'gpt-4.1'
DEFAULT_TEMPERATURE = 0.7
GPT4_TEMPERATURE = 0.3
