# Helm Bot Complete Reference Guide

## 📚 Table of Contents

1. [Installation & Setup](#installation--setup)
2. [Configuration Reference](#configuration-reference)
3. [API Reference](#api-reference)
4. [Usage Patterns](#usage-patterns)
5. [Error Handling](#error-handling)
6. [Advanced Features](#advanced-features)
7. [Troubleshooting](#troubleshooting)
8. [Best Practices](#best-practices)
9. [Examples](#examples)
10. [FAQ](#faq)

---

## 🛠️ Installation & Setup

### System Requirements

```bash
Python >= 3.7
pip >= 20.0
OpenAI API Key
```

### Installation Steps

#### 1. Environment Setup
```bash
# Create virtual environment (recommended)
python -m venv helmbot-env

# Activate virtual environment
# Windows
helmbot-env\Scripts\activate
# macOS/Linux
source helmbot-env/bin/activate
```

#### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 3. Directory Structure Setup
```
your-project/
├── helm-bot.py
├── config.py
├── helm_parser.py
├── llm_manager.py
├── question_manager.py
├── yaml_generator.py
├── requirements.txt
└── sample_helm/              # Your Helm chart directory
    ├── Chart.yaml
    ├── values.yaml           # Optional existing values
    └── templates/
        ├── deployment.yaml
        ├── service.yaml
        └── ...
```

#### 4. API Key Configuration
```bash
# Method 1: Environment variable
export OPENAI_API_KEY="your-api-key-here"

# Method 2: Interactive setup (first run)
python helm-bot.py
# Enter API key when prompted
```

---

## ⚙️ Configuration Reference

### `config.py` Settings

#### Directory Configuration
```python
# Main template directory
TEMPLATE_DIR = 'sample_helm'

# Templates subdirectory
TEMPLATES_SUBDIR = os.path.join(TEMPLATE_DIR, 'templates')
```

#### File Names
```python
# Generated questions file
GENERATED_QUESTIONS_FILE = 'generated_questions.txt'

# Input values file (optional)
VALUES_FILE = 'values.yaml'

# Output generated values file
GENERATED_VALUES_FILE = 'generated_values.yaml'
```

#### LLM Configuration
```python
# Model selection
DEFAULT_MODEL = 'gpt-3.5-turbo'    # For question generation
GPT4_MODEL = 'gpt-4.1'             # For YAML generation

# Temperature settings
DEFAULT_TEMPERATURE = 0.7          # Creative tasks
GPT4_TEMPERATURE = 0.3             # Precision tasks
```

### Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `OPENAI_API_KEY` | OpenAI API authentication | Yes | None |
| `HELM_TEMPLATE_DIR` | Override template directory | No | 'sample_helm' |
| `HELM_QUESTIONS_FILE` | Override questions filename | No | 'generated_questions.txt' |

---

## 🔌 API Reference

### Core Classes

#### `HelmTemplateParser`

```python
class HelmTemplateParser:
    def __init__(self)
    def list_template_files(self) -> List[str]
    def extract_variables(self, files: List[str]) -> Set[str]
```

**Methods:**

- **`list_template_files()`**
  - **Returns**: List of template files (.yaml, .tpl)
  - **Purpose**: Discover Helm template files in the templates directory
  
- **`extract_variables(files)`**
  - **Parameters**: `files` - List of template filenames
  - **Returns**: Set of unique variable names
  - **Purpose**: Extract {{ .Values.* }} variables from templates

#### `LLMManager`

```python
class LLMManager:
    def __init__(self)
    def setup_openai_api(self)
    def get_llm(self, model_name: str, temperature: float) -> ChatOpenAI
    def get_gpt35_llm(self) -> ChatOpenAI
    def get_gpt4_llm(self) -> ChatOpenAI
```

**Methods:**

- **`setup_openai_api()`**
  - **Purpose**: Configure OpenAI API key
  - **Behavior**: Prompts for key if not in environment
  
- **`get_llm(model_name, temperature)`**
  - **Parameters**: Model name and temperature setting
  - **Returns**: Cached ChatOpenAI instance
  - **Purpose**: Get configured LLM instance
  
- **`get_gpt35_llm()`**
  - **Returns**: GPT-3.5 instance with default settings
  
- **`get_gpt4_llm()`**
  - **Returns**: GPT-4 instance with precision settings

#### `QuestionManager`

```python
class QuestionManager:
    def __init__(self, llm_manager: LLMManager, helm_parser: HelmTemplateParser)
    def create_prompt_template(self) -> PromptTemplate
    def ensure_questions_exist(self) -> str
    def generate_questions_for_variables(self, llm, prompt, variables_list) -> str
    def collect_answers(self, questions_path: str) -> List[Tuple[str, str]]
```

**Methods:**

- **`ensure_questions_exist()`**
  - **Returns**: Path to questions file
  - **Purpose**: Generate questions if they don't exist
  
- **`collect_answers(questions_path)`**
  - **Parameters**: Path to questions file
  - **Returns**: List of (question, answer) tuples
  - **Purpose**: Interactive answer collection

#### `YAMLGenerator`

```python
class YAMLGenerator:
    def __init__(self, llm_manager: LLMManager)
    def generate_values_yaml_gpt4(self, answers: List[Tuple[str, str]]) -> str
```

**Methods:**

- **`generate_values_yaml_gpt4(answers)`**
  - **Parameters**: List of (question, answer) tuples
  - **Returns**: Generated YAML content
  - **Purpose**: Create values.yaml from user answers

---

## 🎯 Usage Patterns

### Basic Usage Pattern

```python
# Standard workflow
from helm_parser import HelmTemplateParser
from llm_manager import LLMManager
from question_manager import QuestionManager
from yaml_generator import YAMLGenerator

# Initialize components
parser = HelmTemplateParser()
llm_manager = LLMManager()
question_manager = QuestionManager(llm_manager, parser)
yaml_generator = YAMLGenerator(llm_manager)

# Execute workflow
questions_path = question_manager.ensure_questions_exist()
answers = question_manager.collect_answers(questions_path)
yaml_content = yaml_generator.generate_values_yaml_gpt4(answers)
```

### Custom Question Generation

```python
# Generate questions for specific variables
files = parser.list_template_files()
variables = parser.extract_variables(files)

# Filter variables
specific_vars = [v for v in variables if 'image' in v.lower()]

# Generate questions for subset
llm = llm_manager.get_gpt35_llm()
prompt = question_manager.create_prompt_template()
questions = question_manager.generate_questions_for_variables(
    llm, prompt, specific_vars
)
```

### Programmatic Answer Provision

```python
# Provide answers programmatically
answers = [
    ("What is your application name?", "my-web-app"),
    ("How many replicas?", "3"),
    ("What image repository?", "nginx")
]

yaml_content = yaml_generator.generate_values_yaml_gpt4(answers)
```

---

## 🚨 Error Handling

### Common Exceptions

#### `FileNotFoundError`
```python
# Template directory missing
try:
    files = parser.list_template_files()
except FileNotFoundError:
    print("Template directory not found. Check TEMPLATE_DIR setting.")
```

#### `OpenAI API Errors`
```python
# API key issues
try:
    llm = llm_manager.get_gpt35_llm()
    response = llm.invoke(prompt)
except Exception as e:
    if "authentication" in str(e).lower():
        print("Invalid API key. Please check your OpenAI credentials.")
    elif "rate limit" in str(e).lower():
        print("Rate limit exceeded. Please wait and try again.")
```

#### `Template Parsing Errors`
```python
# Invalid template syntax
try:
    variables = parser.extract_variables(files)
except Exception as e:
    print(f"Template parsing error: {e}")
    print("Check your Helm template syntax.")
```

### Error Recovery Patterns

```python
# Graceful degradation
def safe_generate_questions(question_manager):
    try:
        return question_manager.ensure_questions_exist()
    except Exception as e:
        print(f"Question generation failed: {e}")
        # Fallback to manual question file
        return "manual_questions.txt"
```

---

## 🔧 Advanced Features

### Custom Prompt Templates

```python
# Custom question generation prompt
custom_prompt = PromptTemplate(
    input_variables=['variables', 'chart_name'],
    template="""
    For the Helm chart '{chart_name}' with variables: {variables}
    
    Generate questions that are:
    1. Specific to the application type
    2. Include validation hints
    3. Provide example values
    
    Format each question with:
    - Clear description
    - Example value in parentheses
    - Validation requirements
    """
)
```

### Batch Processing

```python
# Process multiple charts
def process_multiple_charts(chart_directories):
    results = {}
    
    for chart_dir in chart_directories:
        # Update config for each chart
        config.TEMPLATE_DIR = chart_dir
        
        # Process chart
        parser = HelmTemplateParser()
        # ... rest of workflow
        
        results[chart_dir] = yaml_content
    
    return results
```

### Variable Filtering

```python
# Advanced variable filtering
class VariableFilter:
    @staticmethod
    def filter_by_pattern(variables, pattern):
        import re
        regex = re.compile(pattern)
        return [v for v in variables if regex.search(v)]
    
    @staticmethod
    def exclude_common(variables):
        common_vars = {'nameOverride', 'fullnameOverride'}
        return [v for v in variables if v not in common_vars]

# Usage
variables = parser.extract_variables(files)
filtered = VariableFilter.exclude_common(variables)
```

### Custom YAML Templates

```python
# Custom YAML generation template
yaml_template = """
Generate a Kubernetes values.yaml with:

Base structure:
{base_yaml}

User requirements:
{user_answers}

Requirements:
1. Follow Kubernetes best practices
2. Include security defaults
3. Add resource limits
4. Enable monitoring labels
"""
```

---

## 🔍 Troubleshooting

### Common Issues

#### 1. **No Variables Found**

**Problem**: Parser returns empty variable set

**Causes**:
- Templates not using `{{ .Values.* }}` syntax
- Incorrect template directory
- Files not named with .yaml or .tpl extensions

**Solution**:
```python
# Debug variable extraction
files = parser.list_template_files()
print(f"Found files: {files}")

for file in files:
    with open(os.path.join(config.TEMPLATES_SUBDIR, file)) as f:
        content = f.read()
        print(f"Content preview for {file}:")
        print(content[:200])
```

#### 2. **API Rate Limits**

**Problem**: OpenAI API rate limit exceeded

**Solution**:
```python
import time
from functools import wraps

def retry_on_rate_limit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for attempt in range(3):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if "rate limit" in str(e).lower():
                    wait_time = 2 ** attempt
                    print(f"Rate limit hit. Waiting {wait_time}s...")
                    time.sleep(wait_time)
                else:
                    raise
        raise Exception("Max retries exceeded")
    return wrapper
```

#### 3. **Invalid YAML Output**

**Problem**: Generated YAML is malformed

**Solution**:
```python
import yaml

def validate_yaml(yaml_content):
    try:
        yaml.safe_load(yaml_content)
        return True
    except yaml.YAMLError as e:
        print(f"YAML validation error: {e}")
        return False

# Use in generation
yaml_content = yaml_generator.generate_values_yaml_gpt4(answers)
if not validate_yaml(yaml_content):
    print("Regenerating YAML...")
    # Retry logic
```

### Debug Mode

```python
# Enable debug logging
import logging

logging.basicConfig(level=logging.DEBUG)

# Add debug prints
class DebugHelmParser(HelmTemplateParser):
    def extract_variables(self, files):
        print(f"DEBUG: Processing {len(files)} files")
        variables = super().extract_variables(files)
        print(f"DEBUG: Found variables: {variables}")
        return variables
```

---

## 📋 Best Practices

### 1. **Project Organization**

```
project/
├── helmbot/                 # Core bot files
│   ├── helm-bot.py
│   ├── config.py
│   └── ...
├── charts/                  # Helm charts
│   ├── app1/
│   ├── app2/
│   └── ...
├── generated/               # Output files
│   ├── app1-values.yaml
│   ├── app2-values.yaml
│   └── ...
└── configs/                 # Configuration files
    ├── production.py
    ├── staging.py
    └── development.py
```

### 2. **Configuration Management**

```python
# Environment-specific configs
class Config:
    TEMPLATE_DIR = 'sample_helm'
    DEFAULT_MODEL = 'gpt-3.5-turbo'

class ProductionConfig(Config):
    GPT4_MODEL = 'gpt-4'
    DEFAULT_TEMPERATURE = 0.1

class DevelopmentConfig(Config):
    DEFAULT_MODEL = 'gpt-3.5-turbo'
    DEFAULT_TEMPERATURE = 0.8
```

### 3. **Error Handling**

```python
# Comprehensive error handling
def safe_execute_workflow():
    try:
        # Main workflow
        result = execute_helm_bot()
        return {"status": "success", "result": result}
    
    except FileNotFoundError as e:
        return {"status": "error", "type": "file_not_found", "message": str(e)}
    
    except Exception as e:
        if "openai" in str(e).lower():
            return {"status": "error", "type": "api_error", "message": str(e)}
        else:
            return {"status": "error", "type": "unknown", "message": str(e)}
```

### 4. **Performance Optimization**

```python
# Caching and optimization
from functools import lru_cache

class OptimizedLLMManager(LLMManager):
    @lru_cache(maxsize=128)
    def get_cached_response(self, prompt_hash, model_name):
        # Cache responses for identical prompts
        pass
    
    def batch_generate_questions(self, variable_groups):
        # Process multiple variable groups in single API call
        pass
```

### 5. **Testing**

```python
# Unit tests
import unittest
from unittest.mock import Mock, patch

class TestHelmParser(unittest.TestCase):
    def setUp(self):
        self.parser = HelmTemplateParser()
    
    def test_variable_extraction(self):
        # Test variable extraction logic
        content = "{{ .Values.testVar }}"
        variables = self.parser.pattern.findall(content)
        self.assertEqual(variables, ['testVar'])
    
    @patch('builtins.open')
    def test_file_reading(self, mock_open):
        # Test file operations
        mock_open.return_value.__enter__.return_value.read.return_value = "test content"
        # Test logic
```

---

## 📖 Examples

### Example 1: Basic Web Application

**Template Structure**:
```yaml
# deployment.yaml
spec:
  replicas: {{ .Values.replicaCount }}
  template:
    spec:
      containers:
      - name: {{ .Values.appName }}
        image: {{ .Values.image.repository }}:{{ .Values.image.tag }}
        ports:
        - containerPort: {{ .Values.service.port }}
```

**Generated Questions**:
```
1. What is your application name? (Sets the container and app name)
2. How many replicas do you want? (Controls scaling)
3. What image repository should be used? (Docker image location)
4. What image tag/version? (Specific image version)
5. What port should the service expose? (Service port configuration)
```

**User Answers**:
```
1. my-web-app
2. 3
3. nginx
4. 1.21
5. 80
```

**Generated values.yaml**:
```yaml
replicaCount: 3
appName: my-web-app
image:
  repository: nginx
  tag: "1.21"
  pullPolicy: IfNotPresent
service:
  port: 80
  type: ClusterIP
```

### Example 2: Database Application

**Variables Found**:
```
['dbName', 'dbUser', 'dbPassword', 'storageSize', 'storageClass']
```

**Generated Questions**:
```
1. What is the database name? (PostgreSQL database identifier)
2. What username for database access? (Database user account)
3. What password for database user? (Authentication credential)
4. How much storage space needed? (Persistent volume size)
5. What storage class to use? (Storage performance tier)
```

**Generated values.yaml**:
```yaml
postgresql:
  auth:
    database: myapp
    username: appuser
    password: "securepass123"
  primary:
    persistence:
      size: 10Gi
      storageClass: fast-ssd
```

### Example 3: Microservices Application

**Complex Template**:
```yaml
# Multiple services with different configurations
{{- range .Values.services }}
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ .name }}
spec:
  replicas: {{ .replicas | default 1 }}
  template:
    spec:
      containers:
      - image: {{ .image }}:{{ .tag }}
        resources:
          requests:
            memory: {{ .resources.memory }}
            cpu: {{ .resources.cpu }}
{{- end }}
```

**Generated Questions**:
```
1. How many services do you want to deploy? (Number of microservices)
2. For each service, provide: name, image, tag, replicas, memory, cpu
```

**Generated values.yaml**:
```yaml
services:
  - name: auth-service
    image: myapp/auth
    tag: v1.2.0
    replicas: 2
    resources:
      memory: 512Mi
      cpu: 250m
  
  - name: api-service
    image: myapp/api
    tag: v1.2.0
    replicas: 3
    resources:
      memory: 1Gi
      cpu: 500m
```

---

## ❓ FAQ

### Q: Can I use custom OpenAI models?

**A**: Yes, modify the `config.py` file:
```python
DEFAULT_MODEL = 'your-custom-model'
GPT4_MODEL = 'your-gpt4-model'
```

### Q: How do I handle sensitive values like passwords?

**A**: The bot generates placeholder values. Replace them manually or use Kubernetes secrets:
```yaml
# Generated
password: "user-provided-password"

# Recommended for production
password:
  secretRef:
    name: app-secrets
    key: db-password
```

### Q: Can I run this without internet connection?

**A**: No, the bot requires OpenAI API access. Consider:
- Local LLM alternatives (with code modifications)
- Offline question generation (pre-generated questions)

### Q: How do I handle multiple environments?

**A**: Create environment-specific configuration:
```python
# configs/production.py
from config import *
TEMPLATE_DIR = 'charts/production'
GPT4_TEMPERATURE = 0.1

# Usage
import configs.production as config
```

### Q: Can I integrate with CI/CD?

**A**: Yes, create a non-interactive mode:
```python
# Non-interactive execution
def automated_generation(predefined_answers):
    # Skip user input, use predefined answers
    answers = predefined_answers
    return yaml_generator.generate_values_yaml_gpt4(answers)
```

### Q: How do I handle Helm chart dependencies?

**A**: The bot processes template variables only. For dependencies:
1. Configure dependencies in `Chart.yaml`
2. Use `helm dependency update`
3. Run bot on main chart templates

### Q: What if my templates use complex logic?

**A**: The bot extracts basic `{{ .Values.* }}` patterns. For complex templates:
- Simplify variable usage where possible
- Use the bot for basic values, handle complex logic manually
- Consider template restructuring

### Q: How do I validate generated YAML?

**A**: Add validation steps:
```python
import yaml
from kubernetes import client

def validate_k8s_yaml(yaml_content):
    try:
        # Parse YAML
        data = yaml.safe_load(yaml_content)
        
        # Validate against Kubernetes schemas
        # (Implementation depends on your validation needs)
        
        return True
    except Exception as e:
        print(f"Validation error: {e}")
        return False
```

### Q: Can I customize the question format?

**A**: Yes, modify the prompt template in `question_manager.py`:
```python
def create_custom_prompt_template(self):
    return PromptTemplate(
        input_variables=['variables'],
        template="""
        Custom prompt format:
        Variables: {variables}
        
        Generate questions with:
        - Technical context
        - Example values
        - Validation rules
        """
    )
```

---

## 🔗 Related Resources

- [Helm Documentation](https://helm.sh/docs/)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [LangChain Documentation](https://python.langchain.com/docs/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)

---

## 📝 Version History

- **v1.0.0**: Initial release with basic functionality
- **v1.1.0**: Added GPT-4 support for YAML generation
- **v1.2.0**: Enhanced error handling and caching

---

*This reference guide covers all aspects of Helm Bot usage. For additional support, refer to the troubleshooting section or check the project repository for updates.*
