# HelmBot API

FastAPI-based REST API for the HelmBot application that generates Helm chart `values.yaml` files through interactive questions.

## Features

- **GET /questions**: Retrieve list of questions for Helm chart configuration
- **POST /generate-yaml**: Generate `values.yaml` from question-answer pairs
- **Health check endpoint**: Monitor API status
- **Interactive API documentation**: Swagger UI and ReDoc

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Start the API Server

```bash
# From the project root directory
python -m api.server
```

The API will be available at `http://localhost:8000`

### 3. Access API Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## API Endpoints

### GET /questions

Retrieve the list of questions needed to configure a Helm chart.

**Response:**
```json
{
  "questions": [
    "1. What is the name of your application? (Sets the app name used in labels)",
    "2. How many replicas do you want to run? (Controls horizontal scaling)"
  ],
  "total_questions": 2
}
```

### POST /generate-yaml

Generate a `values.yaml` file from question-answer pairs.

**Request Body:**
```json
{
  "qa_pairs": [
    {
      "question": "What is the name of your application?",
      "answer": "my-web-app"
    },
    {
      "question": "How many replicas do you want to run?",
      "answer": "3"
    }
  ]
}
```

**Response:**
```json
{
  "yaml_content": "replicaCount: 3\nimage:\n  repository: my-web-app\n...",
  "file_path": "/path/to/generated_values.yaml",
  "message": "YAML generated successfully"
}
```

## Client Example

Use the provided client example to interact with the API:

```bash
python api/client_example.py
```

## Development

### Project Structure

```
api/
├── __init__.py         # Package initialization
├── main.py            # FastAPI application
├── models.py          # Pydantic models
├── service.py         # Business logic
├── server.py          # Server startup script
├── client_example.py  # Example client
└── README.md          # This file
```

### Running in Development Mode

The server runs with auto-reload enabled by default when using `python -m api.server`.

### Environment Variables

- `OPENAI_API_KEY`: Required for LLM operations
- `HOST`: Server host (default: 0.0.0.0)
- `PORT`: Server port (default: 8000)

## Error Handling

The API provides structured error responses:

```json
{
  "error": "Error description",
  "detail": "Detailed error information"
}
```

Common HTTP status codes:
- `200`: Success
- `400`: Bad request (invalid input)
- `500`: Internal server error

## Integration

This API can be integrated with:
- Web frontends (React, Vue, Angular)
- Mobile applications
- CI/CD pipelines
- Command-line tools
- Other microservices

## Security Considerations

For production deployment:
1. Configure CORS properly in `main.py`
2. Add authentication/authorization
3. Use HTTPS
4. Set up proper logging
5. Configure rate limiting
