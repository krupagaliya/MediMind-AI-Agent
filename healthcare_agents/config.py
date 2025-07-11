"""
Configuration file for the Healthcare Agent System
Clean and minimal configuration for Genai with Vertex AI
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class HealthcareAgentConfig:
    """Clean configuration settings for the healthcare agent system"""
    
    # Google AI API Configuration
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")
    GOOGLE_GENAI_USE_VERTEXAI = os.getenv("GOOGLE_GENAI_USE_VERTEXAI", "False").lower() == "true"
    
    # Google Cloud Configuration (for Vertex AI)
    GOOGLE_CLOUD_PROJECT = os.getenv("GOOGLE_CLOUD_PROJECT", "")
    GOOGLE_CLOUD_LOCATION = os.getenv("GOOGLE_CLOUD_LOCATION", "us-central1")
    
    # API Keys for Agent Tools
    GOOGLE_PLACES_API_KEY = os.getenv("GOOGLE_PLACES_API_KEY", "")
    
    # Model Configuration
    DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "gemini-2.0-flash")
    
    # India-specific Configuration
    EMERGENCY_NUMBER = "108"  # India Emergency Number
    
    @classmethod
    def validate_config(cls) -> list:
        """Validate essential configuration and return any missing requirements"""
        missing = []
        
        if not cls.GOOGLE_API_KEY:
            missing.append("GOOGLE_API_KEY is required")
        
        if cls.GOOGLE_GENAI_USE_VERTEXAI and not cls.GOOGLE_CLOUD_PROJECT:
            missing.append("GOOGLE_CLOUD_PROJECT is required when using Vertex AI")
        
        if not cls.GOOGLE_PLACES_API_KEY:
            missing.append("GOOGLE_PLACES_API_KEY is required for hospital finder")
        
        return missing
    
    @classmethod
    def is_vertex_ai_enabled(cls) -> bool:
        """Check if Vertex AI is enabled and properly configured"""
        return cls.GOOGLE_GENAI_USE_VERTEXAI and bool(cls.GOOGLE_CLOUD_PROJECT)

# Create a global config instance
config = HealthcareAgentConfig() 