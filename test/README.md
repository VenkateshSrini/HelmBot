# HelmBot Test Suite

This folder contains all test and demo files for the HelmBot application.

## Test Files

### Core Functionality Tests

- **`test_llm_claude.py`** - Tests LLM manager with Anthropic Claude integration
- **`test_bedrock.py`** - Tests AWS Bedrock provider integration and functionality
- **`test_complete_flow.py`** - End-to-end test of the complete HelmBot workflow
- **`test_service.py`** - Tests the API service layer functionality

### Configuration Tests

- **`test_api_key_prompting.py`** - Tests API key prompting behavior for different providers

### Demo Scripts

- **`demo_api_setup.py`** - Demonstrates API key setup and configuration status
- **`demo_multi_provider.py`** - Interactive demo of all three AI providers (OpenAI, Anthropic, Bedrock)

### Test Utilities

- **`run_all_tests.py`** - Test runner that executes all tests in sequence

## Running Tests

### Run All Tests
```bash
# From the HelmBot root directory
python test/run_all_tests.py
```

### Run Individual Tests
```bash
# From the HelmBot root directory
python test/test_llm_claude.py       # Test Anthropic Claude
python test/test_bedrock.py          # Test AWS Bedrock (requires AWS credentials)
python test/test_complete_flow.py    # End-to-end workflow test
python test/test_service.py          # API service tests
python test/test_api_key_prompting.py

# Run demos
python test/demo_api_setup.py        # Configuration demo
python test/demo_multi_provider.py   # Multi-provider interactive demo
```

### AWS Bedrock Testing

The `test_bedrock.py` file tests AWS Bedrock integration:

**Prerequisites:**
- Install AWS dependencies: `pip install langchain-aws boto3`
- AWS credentials configured (one of):
  - Environment variables: `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_DEFAULT_REGION`
  - AWS CLI configured: `aws configure`
  - IAM role (if running on AWS infrastructure)

**Usage:**
```bash
# Test Bedrock provider (will prompt for credentials if needed)
python test/test_bedrock.py

# Or use the multi-provider demo for interactive testing
python test/demo_multi_provider.py
```

**Required AWS Permissions:**
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "bedrock:InvokeModel",
                "bedrock:ListFoundationModels"
            ],
            "Resource": "*"
        }
    ]
}
```

## Test Requirements

All tests require the same dependencies as the main application:
- Python virtual environment activated
- Required packages installed (`pip install -r requirements.txt`)
- Appropriate API keys configured (tests will prompt if missing)

## Test Structure

Each test file:
1. Sets up the correct Python path to import HelmBot modules
2. Tests specific functionality in isolation
3. Provides clear output indicating success/failure
4. Includes error handling and debugging information

## Notes

- Tests may prompt for API keys if not set in environment variables
- Some tests require actual API calls to LLM providers
- Tests are designed to be run independently or as a suite
- All test files are self-contained and don't modify core application code