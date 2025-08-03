# Helm Bot

An intelligent assistant that simplifies Helm chart configuration by automatically generating user-friendly questions and creating `values.yaml` files using AI.

## 🚀 Overview

Helm Bot is a Python application that leverages OpenAI's GPT models to streamline the process of configuring Helm charts. Instead of manually editing complex YAML files, users can answer simple questions and let the bot generate the appropriate configuration.

## ✨ Features

- **Automatic Variable Detection**: Scans Helm templates to identify all configurable variables
- **Intelligent Question Generation**: Uses GPT-3.5 to create user-friendly questions for each variable
- **Smart YAML Generation**: Employs GPT-4 to merge user answers with existing values.yaml
- **Template Analysis**: Supports standard Helm template files (.yaml, .tpl)
- **Interactive CLI**: Simple command-line interface for easy interaction

## 🏗️ Architecture

The application follows a modular design with five core components:

- **`helm_parser.py`**: Parses Helm templates and extracts variables
- **`llm_manager.py`**: Manages OpenAI API interactions and model instances
- **`question_manager.py`**: Generates questions and collects user answers
- **`yaml_generator.py`**: Creates final values.yaml using AI
- **`config.py`**: Centralized configuration management

## 📋 Prerequisites

- Python 3.7 or higher
- OpenAI API key
- Helm chart templates in the `sample_helm/templates/` directory

## 🛠️ Installation

1. **Clone or download the project**:
   ```bash
   git clone <repository-url>
   cd helmbot
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your Helm chart**:
   - Place your Helm chart in the `sample_helm/` directory
   - Ensure templates are in `sample_helm/templates/`
   - Include a `Chart.yaml` file

## 🚀 Quick Start

1. **Run the application**:
   ```bash
   python helm-bot.py
   ```

2. **Enter your OpenAI API key** when prompted (first run only)

3. **Answer the generated questions** about your Helm chart configuration

4. **Review the generated `generated_values.yaml`** file

## 📁 Project Structure

```
helmbot/
├── helm-bot.py              # Main application entry point
├── config.py                # Configuration settings
├── helm_parser.py           # Template parsing logic
├── llm_manager.py           # OpenAI API management
├── question_manager.py      # Question generation and collection
├── yaml_generator.py        # YAML file generation
├── requirements.txt         # Python dependencies
├── helmbot-notebook.ipynb   # Jupyter notebook version
└── sample_helm/             # Sample Helm chart
    ├── Chart.yaml
    ├── values.yaml
    ├── generated_values.yaml
    ├── generated_questions.txt
    └── templates/
        ├── deployment.yaml
        ├── service.yaml
        ├── ingress.yaml
        └── ...
```

## 🔧 Configuration

The `config.py` file contains all configurable settings:

- **Template Directory**: `TEMPLATE_DIR = 'sample_helm'`
- **Models**: GPT-3.5 for questions, GPT-4 for YAML generation
- **Temperature**: 0.7 for questions, 0.3 for YAML (more precise)

## 📖 Usage Examples

### Basic Usage
```bash
python helm-bot.py
```

### Using the Jupyter Notebook
Open `helmbot-notebook.ipynb` for an interactive experience with step-by-step execution.

## 🤖 How It Works

1. **Template Scanning**: The bot scans your Helm templates for variables using regex patterns
2. **Question Generation**: GPT-3.5 creates user-friendly questions for each variable
3. **Answer Collection**: Interactive CLI collects user responses
4. **YAML Generation**: GPT-4 merges answers with existing values.yaml structure
5. **Output**: Generates `generated_values.yaml` ready for Helm deployment

## 🔍 Example Output

**Generated Questions**:
```
1. What is the name of your application? (Sets the app name used in labels)
2. How many replicas do you want to run? (Controls horizontal scaling)
3. What container image should be used? (Specifies the Docker image)
```

**Generated values.yaml**:
```yaml
replicaCount: 3
image:
  repository: myapp
  tag: v1.0
  pullPolicy: IfNotPresent
```

## 🚨 Error Handling

- **Missing API Key**: Prompts user to enter OpenAI API key
- **Missing Templates**: Provides clear error messages for missing files
- **Invalid Responses**: Graceful handling of API errors and timeouts

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For issues and questions:
1. Check the existing documentation
2. Review error messages carefully
3. Ensure your OpenAI API key has sufficient credits
4. Verify Helm template syntax

## 🔮 Future Enhancements

- Support for multiple Helm charts
- Integration with Helm CLI
- Custom question templates
- Advanced YAML validation
- Web interface option
