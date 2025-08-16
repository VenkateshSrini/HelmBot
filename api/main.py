"""
FastAPI main application
"""
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import List

from .models import (
    QuestionResponse, 
    GenerateYAMLRequest, 
    ErrorResponse,
    QAItem
)
from .service import HelmBotService

# Create FastAPI app
app = FastAPI(
    title="HelmBot API",
    description="API for generating Helm chart values.yaml files through interactive questions",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure as needed for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize service
helm_service = HelmBotService()


@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "HelmBot API is running", "version": "1.0.0"}


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


@app.get("/questions", response_model=QuestionResponse)
async def get_questions():
    """
    Get list of questions for Helm chart configuration.
    
    Returns:
        QuestionResponse: List of questions and total count
    """
    try:
        questions = helm_service.get_questions()
        return QuestionResponse(
            questions=questions,
            total_questions=len(questions)
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to retrieve questions: {str(e)}"
        )


@app.post("/generate-yaml")
async def generate_yaml(request: GenerateYAMLRequest):
    """
    Generate values.yaml file from question-answer pairs.
    
    Args:
        request: GenerateYAMLRequest containing list of question-answer pairs
        
    Returns:
        GenerateYAMLResponse: Generated YAML content and file path
    """
    try:
        if not request.qa_pairs:
            raise HTTPException(
                status_code=400,
                detail="No question-answer pairs provided"
            )
        
        # Convert QAItem objects to tuples
        qa_tuples = [(qa.question, qa.answer) for qa in request.qa_pairs]
        
        # Generate YAML
        _, file_path = helm_service.generate_yaml(qa_tuples)
        
        # Return the YAML file for download
        return FileResponse(
            path=file_path,
            media_type="application/x-yaml",
            filename="generated_values.yaml"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to generate YAML: {str(e)}"
        )


# Error handlers
@app.exception_handler(404)
async def not_found_handler(request, exc):
    return {"error": "Endpoint not found", "detail": str(exc)}


@app.exception_handler(500)
async def internal_error_handler(request, exc):
    return {"error": "Internal server error", "detail": str(exc)}
