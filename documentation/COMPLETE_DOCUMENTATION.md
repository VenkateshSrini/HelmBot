# HelmBot - Comprehensive Documentation

**AI-Powered Helm Chart Configuration Assistant**

*Version: 2.0 | Updated: September 2025*

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Architecture](#architecture)
4. [Installation & Setup](#installation--setup)
5. [Configuration](#configuration)
6. [AI Provider Management](#ai-provider-management)
7. [Usage Guide](#usage-guide)
8. [API Reference](#api-reference)
9. [Testing](#testing)
10. [Implementation Details](#implementation-details)
11. [Troubleshooting](#troubleshooting)
12. [Advanced Topics](#advanced-topics)
13. [Contributing](#contributing)

---

## 🚀 Overview

HelmBot is an intelligent Python application that revolutionizes Helm chart configuration by leveraging advanced AI models to automatically generate user-friendly questions and create optimized `values.yaml` files. Instead of manually editing complex YAML configurations, users simply answer intuitive questions and let AI handle the technical implementation.

### Key Benefits
- **Simplifies Complex Configurations**: Transforms technical Helm templates into user-friendly questions
- **AI-Powered Intelligence**: Uses advanced language models for contextual understanding
- **Multi-Provider Support**: Works with OpenAI GPT and Anthropic Claude models
- **Production Ready**: Includes REST API, comprehensive testing, and enterprise features
- **Extensible Architecture**: Modular design supports easy customization and extension

---

## ✨ Features

### Core Capabilities
- **🔍 Automatic Variable Detection**: Intelligently scans Helm templates to identify all configurable variables
- **❓ Smart Question Generation**: Uses AI to create context-aware, user-friendly questions
- **🎯 Intelligent YAML Generation**: Employs advanced AI models to merge answers with existing configurations
- **📊 Template Analysis**: Supports all standard Helm template files (.yaml, .tpl, .yml)
- **💻 Interactive CLI**: Intuitive command-line interface for streamlined workflows
- **🌐 REST API**: FastAPI-based web service for integration with web applications
- **🔄 Multi-Provider AI**: Seamlessly switch between OpenAI and Anthropic models

### Advanced Features
- **📁 Project Structure Management**: Organized documentation, testing, and API layers
- **🧪 Comprehensive Testing Suite**: Automated tests for all components and integrations
- **🔑 Smart API Key Management**: Automatic prompting and environment variable support
- **📖 Rich Documentation**: Complete guides for users, developers, and administrators
- **🐳 Container Support**: Docker configuration for easy deployment
- **⚡ Performance Optimization**: Intelligent caching and efficient resource management

---

## 🏗️ Architecture

### System Design Philosophy

HelmBot follows a **modular, factory-pattern architecture** designed for maintainability, extensibility, and robust error handling.

### Core Components

```
HelmBot/
├── 🎯 Core Engine
│   ├── helm-bot.py           # Main application orchestrator
│   ├── config.py             # Centralized configuration management
│   ├── helm_parser.py        # Template analysis and variable extraction
│   ├── llm_manager.py        # AI provider management with factory pattern
│   ├── question_manager.py   # Question generation and answer collection
│   └── yaml_generator.py     # Intelligent YAML generation
├── 🌐 API Layer
│   ├── main.py              # FastAPI application
│   ├── models.py            # Pydantic data models
│   ├── service.py           # Business logic layer
│   └── server.py            # Server startup and configuration
├── 📚 Documentation
│   └── [comprehensive guides and references]
├── 🧪 Testing Suite
│   └── [comprehensive test coverage]
└── 📁 Assets
    ├── sample_helm/         # Sample Helm chart for demonstration
    └── requirements.txt     # Dependency management
```

### Architecture Patterns

#### Factory Pattern for AI Providers
```python
ModelProviderFactory
├── OpenAIProvider    # GPT-3.5, GPT-4 support
└── AnthropicProvider # Claude Sonnet support
```

#### Workflow Pipeline
```
Template Scanning → Variable Extraction → Question Generation → 
User Interaction → AI Processing → YAML Generation → Output
```

---

## 🛠️ Installation & Setup

### System Requirements

```bash
Python >= 3.7
pip >= 20.0
AI API Key (OpenAI or Anthropic)
```

### Quick Installation

#### 1. **Environment Setup**
```bash
# Clone the repository
git clone <repository-url>
cd HelmBot

# Create virtual environment (recommended)
python -m venv .venv

# Activate virtual environment
# Windows PowerShell
.venv\Scripts\Activate.ps1
# Windows CMD
.venv\Scripts\activate.bat
# macOS/Linux
source .venv/bin/activate
```

#### 2. **Install Dependencies**
```bash
pip install -r requirements.txt
```

#### 3. **API Key Configuration**

**Option A: Environment Variables**
```powershell
# For Anthropic Claude (current default)
$env:ANTHROPIC_API_KEY="your-anthropic-api-key"

# For OpenAI GPT
$env:OPENAI_API_KEY="your-openai-api-key"
```

**Option B: Interactive Setup**
The application will prompt for API keys if not found in environment variables.

#### 4. **Verify Installation**
```bash
python test/demo_api_setup.py
```

### Directory Structure Setup

```
your-project/
├── [HelmBot files]
└── sample_helm/              # Your Helm chart
    ├── Chart.yaml
    ├── values.yaml           # Optional existing values
    └── templates/
        ├── deployment.yaml
        ├── service.yaml
        ├── ingress.yaml
        └── [other templates]
```

---

## ⚙️ Configuration

### Core Configuration (`config.py`)

```python
# Directory paths
TEMPLATE_DIR = 'sample_helm'
TEMPLATES_SUBDIR = 'sample_helm/templates'

# File names
GENERATED_QUESTIONS_FILE = 'generated_questions.txt'
VALUES_FILE = 'values.yaml'
GENERATED_VALUES_FILE = 'generated_values.yaml'

# AI Provider Configuration
PROVIDER = 'anthropic'  # Options: 'openai', 'anthropic'

# Model Settings (Current: Claude Sonnet 4)
DEFAULT_MODEL = 'claude-sonnet-4-20250514'
GPT4_MODEL = 'claude-sonnet-4-20250514'

# Temperature Settings
DEFAULT_TEMPERATURE = 0.7  # For creative tasks (questions)
GPT4_TEMPERATURE = 0.3     # For precise tasks (YAML generation)
```

### Customization Options

- **Template Directory**: Change `TEMPLATE_DIR` to point to your Helm chart
- **Output Location**: Modify file paths for different project structures
- **Model Selection**: Switch between different AI models and providers
- **Temperature Tuning**: Adjust creativity vs. precision for different use cases

---

## 🤖 AI Provider Management

### Supported Providers

| Provider | Models | Use Cases | API Required |
|----------|--------|-----------|--------------|
| **Anthropic** | Claude Sonnet 4 | Advanced reasoning, large context | `ANTHROPIC_API_KEY` |
| **OpenAI** | GPT-3.5, GPT-4 | General purpose, established | `OPENAI_API_KEY` |

### Provider Configuration

#### Current Setup (Anthropic Claude Sonnet 4)
```python
PROVIDER = 'anthropic'
DEFAULT_MODEL = 'claude-sonnet-4-20250514'
```

#### Switching to OpenAI
```python
PROVIDER = 'openai'
DEFAULT_MODEL = 'gpt-3.5-turbo'
GPT4_MODEL = 'gpt-4.1'
```

### API Key Management

The system provides **intelligent API key management**:

1. **Automatic Detection**: Checks environment variables first
2. **Interactive Prompting**: Asks for keys if not found
3. **Helpful Guidance**: Provides links to get API keys
4. **Validation**: Ensures keys are properly formatted
5. **Session Persistence**: Remembers keys for the current session

### Provider Factory Architecture

```python
# Extensible factory pattern
class ModelProviderFactory:
    _providers = {
        'openai': OpenAIProvider,
        'anthropic': AnthropicProvider
        # Easy to add: 'google': GoogleProvider, etc.
    }
```

---

## 📖 Usage Guide

### Command Line Interface

#### Basic Usage
```bash
# Run the main application
python helm-bot.py
```

#### Workflow Steps
1. **Template Analysis**: Scans your Helm chart for variables
2. **Question Generation**: AI creates user-friendly questions
3. **Interactive Input**: Answer questions about your configuration
4. **YAML Generation**: AI merges answers into optimized values.yaml
5. **Review Output**: Examine generated configuration file

### Web API Interface

#### Start API Server
```bash
# Start FastAPI server
python -m api.server

# Access Swagger UI
# http://localhost:8000/docs
```

#### API Endpoints

**GET /questions** - Retrieve configuration questions
```bash
curl http://localhost:8000/questions
```

**POST /generate-yaml** - Generate values.yaml from answers
```bash
curl -X POST "http://localhost:8000/generate-yaml" \
     -H "Content-Type: application/json" \
     -d '{
       "qa_pairs": [
         {"question": "App name?", "answer": "my-app"},
         {"question": "Replicas?", "answer": "3"}
       ]
     }'
```

### Example Workflow

#### Input: Helm Template
```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ .Values.appName }}
spec:
  replicas: {{ .Values.replicaCount }}
  template:
    spec:
      containers:
      - image: {{ .Values.image.repository }}:{{ .Values.image.tag }}
```

#### Generated Questions
```
1. What is the name of your application? (Sets the app name used in labels)
2. How many replicas do you want to run? (Controls horizontal scaling)
3. What Docker image repository should be used? (Specifies the container image)
4. What image tag should be deployed? (Version or environment identifier)
```

#### Generated values.yaml
```yaml
appName: "my-web-application"
replicaCount: 3
image:
  repository: "nginx"
  tag: "1.21"
  pullPolicy: "IfNotPresent"
```

---

## 🌐 API Reference

### FastAPI Web Service

#### Server Configuration
```python
# Default configuration
Host: 0.0.0.0
Port: 8000
Reload: True (development)
CORS: Enabled for all origins
```

#### Endpoint Details

##### GET /questions
**Purpose**: Retrieve generated questions for Helm chart configuration

**Response Model**:
```json
{
  "questions": ["string"],
  "total_questions": "integer"
}
```

**Example Response**:
```json
{
  "questions": [
    "1. What is your application name? (Sets app metadata)",
    "2. How many replicas? (Controls scaling)"
  ],
  "total_questions": 2
}
```

##### POST /generate-yaml
**Purpose**: Generate values.yaml from question-answer pairs

**Request Model**:
```json
{
  "qa_pairs": [
    {
      "question": "string",
      "answer": "string"
    }
  ]
}
```

**Response**: Downloads generated YAML file directly

##### GET /health
**Purpose**: Health check endpoint for monitoring

**Response**:
```json
{
  "status": "healthy"
}
```

#### Interactive Documentation

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

### Client Integration

#### Python Client Example
```python
import requests

# Get questions
response = requests.get("http://localhost:8000/questions")
questions = response.json()["questions"]

# Generate YAML
qa_pairs = [
    {"question": questions[0], "answer": "my-app"},
    {"question": questions[1], "answer": "3"}
]

response = requests.post(
    "http://localhost:8000/generate-yaml",
    json={"qa_pairs": qa_pairs}
)

# Download generated YAML file
with open("values.yaml", "wb") as f:
    f.write(response.content)
```

#### JavaScript/Frontend Integration
```javascript
// Fetch questions
const questionsResponse = await fetch('/questions');
const { questions } = await questionsResponse.json();

// Submit answers and download YAML
const qaResponse = await fetch('/generate-yaml', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ qa_pairs: answers })
});

const blob = await qaResponse.blob();
const url = URL.createObjectURL(blob);
// Trigger download
```

---

## 🧪 Testing

### Test Suite Organization

```
test/
├── Core Tests
│   ├── test_llm_claude.py          # AI provider integration
│   ├── test_complete_flow.py       # End-to-end workflow
│   └── test_service.py             # API service functionality
├── Configuration Tests
│   └── test_api_key_prompting.py   # API key management
├── Demo Scripts
│   └── demo_api_setup.py           # Configuration demonstration
├── Utilities
│   └── run_all_tests.py            # Automated test runner
└── README.md                       # Testing documentation
```

### Running Tests

#### Comprehensive Test Suite
```bash
# Run all tests
python test/run_all_tests.py

# Run specific test categories
python test/test_llm_claude.py
python test/test_complete_flow.py
python test/test_service.py
```

#### Configuration Demo
```bash
# Check current configuration
python test/demo_api_setup.py
```

### Test Coverage

- **✅ AI Provider Integration**: Verify Claude Sonnet 4 functionality
- **✅ Question Generation**: Test intelligent question creation
- **✅ YAML Generation**: Validate output quality and format
- **✅ API Endpoints**: Comprehensive REST API testing
- **✅ Error Handling**: Robust error scenarios and recovery
- **✅ Configuration Management**: Provider switching and setup

---

## 🔧 Implementation Details

### Technical Architecture

#### AI Provider Factory Pattern
```python
class ModelProviderFactory:
    """Extensible factory for AI providers"""
    
    @classmethod
    def create_provider(cls, provider_name: str) -> ModelProvider:
        """Create provider instance with automatic configuration"""
        # Handles OpenAI, Anthropic, and future providers
```

#### Intelligent Caching
```python
class LLMManager:
    def __init__(self):
        self._llm_cache = {}  # Performance optimization
        
    def get_llm(self, model_name, temperature):
        cache_key = f"{model_name}_{temperature}"
        if cache_key not in self._llm_cache:
            self._llm_cache[cache_key] = self.provider.create_llm(...)
```

#### Variable Extraction Algorithm
```python
# Regex pattern for Helm template variables
pattern = re.compile(r'\{\{\s*\.Values\.([a-zA-Z0-9_]+)')

# Supports nested variables and complex template structures
# Examples: {{ .Values.app.name }}, {{.Values.replicaCount}}
```

### Performance Optimizations

1. **Model Instance Caching**: Reuse expensive AI model instances
2. **Lazy Loading**: Initialize components only when needed  
3. **Batch Processing**: Single API call for multiple operations
4. **Efficient Parsing**: Optimized regex for template scanning
5. **Memory Management**: Proper cleanup and resource management

### Error Handling Strategy

```python
# Comprehensive error handling at each layer
try:
    # AI provider operations
    result = ai_provider.generate(prompt)
except ProviderError as e:
    # Provider-specific error handling
    logger.error(f"AI provider error: {e}")
    # Graceful degradation or retry logic
except Exception as e:
    # General error handling
    logger.error(f"Unexpected error: {e}")
    # User-friendly error messages
```

### Security Considerations

- **API Key Protection**: Secure handling of sensitive credentials
- **Input Validation**: Comprehensive validation of user inputs
- **Output Sanitization**: Safe YAML generation without injection risks
- **CORS Configuration**: Proper cross-origin request handling
- **Rate Limiting**: Built-in protection against abuse (configurable)

---

## 🔍 Troubleshooting

### Common Issues and Solutions

#### 1. API Key Issues
**Problem**: "API key not found" or authentication errors

**Solutions**:
```bash
# Check environment variables
echo $ANTHROPIC_API_KEY  # Linux/Mac
echo $env:ANTHROPIC_API_KEY  # Windows PowerShell

# Set API key
export ANTHROPIC_API_KEY="your-key"  # Linux/Mac
$env:ANTHROPIC_API_KEY="your-key"    # Windows PowerShell

# Verify API key format
# Anthropic: sk-ant-api03-...
# OpenAI: sk-...
```

#### 2. Template Parsing Issues
**Problem**: No variables found or parsing errors

**Solutions**:
- Verify Helm template syntax: `{{ .Values.variableName }}`
- Check file extensions: `.yaml`, `.yml`, `.tpl`
- Ensure templates are in `sample_helm/templates/` directory
- Validate template structure with `helm template`

#### 3. AI Model Issues
**Problem**: Model not found or API errors

**Solutions**:
```python
# Update model identifiers in config.py
# Anthropic Claude Sonnet 4
DEFAULT_MODEL = 'claude-sonnet-4-20250514'

# OpenAI models  
DEFAULT_MODEL = 'gpt-3.5-turbo'
GPT4_MODEL = 'gpt-4.1'
```

#### 4. Import and Path Issues
**Problem**: Module import errors

**Solutions**:
```bash
# Ensure proper Python path
export PYTHONPATH="${PYTHONPATH}:$(pwd)"

# Activate virtual environment
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\Activate.ps1  # Windows

# Reinstall dependencies
pip install -r requirements.txt
```

#### 5. FastAPI Server Issues
**Problem**: Server won't start or API endpoints not accessible

**Solutions**:
```bash
# Check port availability
netstat -an | grep 8000

# Start with different port
uvicorn api.main:app --port 8001

# Check firewall settings
# Ensure port 8000 is open for local development
```

### Debug Mode

Enable verbose logging for troubleshooting:
```python
# Add to config.py
DEBUG_MODE = True
LOG_LEVEL = 'DEBUG'

# Run with verbose output
python helm-bot.py --verbose
```

### Getting Help

1. **Check Error Messages**: HelmBot provides detailed error descriptions
2. **Review Logs**: Check application logs for specific error details
3. **Test Configuration**: Run `python test/demo_api_setup.py`
4. **Validate Environment**: Ensure all dependencies are properly installed
5. **API Documentation**: Use Swagger UI for API troubleshooting

---

## 🚀 Advanced Topics

### Custom AI Providers

#### Adding New Providers
```python
class CustomProvider(ModelProvider):
    """Example: Google Gemini Provider"""
    
    def setup_api_key(self):
        # Custom API key handling
        pass
    
    def create_llm(self, model_name, temperature):
        # Custom model instantiation
        pass
    
    def get_provider_name(self):
        return "Google Gemini"

# Register in factory
ModelProviderFactory._providers['google'] = CustomProvider
```

### Extended Configuration

#### Environment-Specific Settings
```python
# config.py
import os

# Environment-based configuration
ENV = os.getenv('HELMBOT_ENV', 'development')

if ENV == 'production':
    DEFAULT_TEMPERATURE = 0.1  # More conservative
    DEBUG_MODE = False
elif ENV == 'development':
    DEFAULT_TEMPERATURE = 0.7  # More creative
    DEBUG_MODE = True
```

#### Custom Question Templates
```python
# Custom prompt templates
CUSTOM_QUESTION_TEMPLATE = """
Given these Helm variables: {variables}

Generate questions that are:
1. Business-focused rather than technical
2. Include examples for clarity
3. Group related concepts together

Format: numbered list with explanations
"""
```

### Integration Patterns

#### CI/CD Integration
```bash
#!/bin/bash
# ci-integration.sh

# Generate values.yaml in CI pipeline
export ANTHROPIC_API_KEY="${CI_ANTHROPIC_KEY}"

# Run HelmBot with predefined answers
python helm-bot.py --answers-file ci-answers.json

# Validate generated YAML
helm template ./sample_helm --values generated_values.yaml
```

#### Kubernetes Operator Integration
```python
# Example: Kubernetes operator integration
class HelmBotOperator:
    def reconcile(self, helm_chart_resource):
        # Use HelmBot to generate values.yaml
        service = HelmBotService()
        questions = service.get_questions()
        
        # Apply business logic for automated answers
        answers = self.generate_automated_answers(questions)
        
        # Generate and apply configuration
        yaml_content = service.generate_yaml(answers)
        self.apply_helm_chart(yaml_content)
```

### Performance Tuning

#### Optimization Strategies
```python
# config.py performance settings
LLM_CACHE_SIZE = 10  # Maximum cached model instances
REQUEST_TIMEOUT = 30  # AI API timeout (seconds)
BATCH_SIZE = 5      # Questions per AI request

# Memory optimization
LAZY_LOADING = True
CLEANUP_INTERVAL = 3600  # Cleanup cache every hour
```

### Monitoring and Observability

#### Logging Configuration
```python
import logging

# Structured logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('helmbot.log'),
        logging.StreamHandler()
    ]
)

# Custom metrics
class HelmBotMetrics:
    def __init__(self):
        self.questions_generated = 0
        self.yaml_files_created = 0
        self.api_calls_made = 0
```

---

## 🤝 Contributing

### Development Setup

#### 1. Fork and Clone
```bash
git clone https://github.com/yourusername/HelmBot.git
cd HelmBot
```

#### 2. Development Environment
```bash
# Create development environment
python -m venv dev-env
source dev-env/bin/activate  # or dev-env\Scripts\Activate.ps1

# Install with development dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt  # If available
```

#### 3. Pre-commit Setup
```bash
# Install pre-commit hooks
pre-commit install

# Run tests before committing
python test/run_all_tests.py
```

### Contribution Guidelines

#### Code Standards
- **Python Style**: Follow PEP 8 guidelines
- **Documentation**: Comprehensive docstrings for all functions
- **Type Hints**: Use type annotations for better code clarity
- **Error Handling**: Implement robust error handling and logging
- **Testing**: Include tests for all new functionality

#### Pull Request Process
1. **Create Feature Branch**: `git checkout -b feature/your-feature-name`
2. **Implement Changes**: Follow coding standards and best practices
3. **Add Tests**: Ensure comprehensive test coverage
4. **Update Documentation**: Keep documentation current
5. **Submit PR**: Provide clear description of changes and rationale

#### Areas for Contribution
- **New AI Providers**: Add support for additional AI services
- **Enhanced Templates**: Improve question generation templates
- **Web Interface**: Develop browser-based user interface
- **Helm Integration**: Direct integration with Helm CLI commands
- **Performance**: Optimization and caching improvements
- **Security**: Enhanced security features and best practices

### Release Process

#### Version Management
```bash
# Update version in setup.py and __init__.py
# Create release notes
# Tag release
git tag -a v2.1.0 -m "Release version 2.1.0"
git push origin v2.1.0
```

---

## 📄 License and Support

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Support and Community
- **GitHub Issues**: Report bugs and request features
- **Documentation**: Comprehensive guides and references
- **Testing**: Extensive test suite for reliability
- **Community**: Contributing guidelines and development resources

### Acknowledgments
- **Anthropic**: Claude AI models for advanced language understanding
- **OpenAI**: GPT models for conversational AI capabilities
- **FastAPI**: Modern web framework for API development
- **Helm Community**: Kubernetes package management ecosystem

---

**End of Documentation**

*This comprehensive guide covers all aspects of HelmBot from basic usage to advanced customization. For specific questions or issues not covered here, please refer to the GitHub repository or create an issue for community support.*