# HelmBot Test Suite

This folder contains all test and demo files for the HelmBot application.

## Test Files

### Core Functionality Tests

- **`test_llm_claude.py`** - Tests LLM manager with Anthropic Claude integration
- **`test_complete_flow.py`** - End-to-end test of the complete HelmBot workflow
- **`test_service.py`** - Tests the API service layer functionality

### Configuration Tests

- **`test_api_key_prompting.py`** - Tests API key prompting behavior for different providers

### Demo Scripts

- **`demo_api_setup.py`** - Demonstrates API key setup and configuration status

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
python test/test_llm_claude.py
python test/test_complete_flow.py
python test/test_service.py
python test/test_api_key_prompting.py

# Run demo
python test/demo_api_setup.py
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