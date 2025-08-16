"""
Pydantic models for API requests and responses
"""
from typing import List, Tuple
from pydantic import BaseModel, Field


class QuestionResponse(BaseModel):
    """Response model for questions endpoint"""
    questions: List[str] = Field(..., description="List of generated questions")
    total_questions: int = Field(..., description="Total number of questions")


class QAItem(BaseModel):
    """Model for a single question-answer pair"""
    question: str = Field(..., description="The question")
    answer: str = Field(..., description="The answer")


class GenerateYAMLRequest(BaseModel):
    """Request model for YAML generation"""
    qa_pairs: List[QAItem] = Field(..., description="List of question-answer pairs")


class GenerateYAMLResponse(BaseModel):
    """Response model for YAML generation"""
    yaml_content: str = Field(..., description="Generated YAML content")
    file_path: str = Field(..., description="Path where the YAML file was saved")
    message: str = Field(..., description="Success message")


class ErrorResponse(BaseModel):
    """Error response model"""
    error: str = Field(..., description="Error message")
    detail: str = Field(None, description="Detailed error information")
