"""
Agent 1: Symptom Analysis Agent
Clean and simple agent that only uses Google Search for medical information
All prompts are stored in prompt.py
"""

import os
from dotenv import load_dotenv
from google.adk.agents import LlmAgent
from google.adk.tools import google_search
from .prompt import SYMPTOM_ANALYZER_PROMPT
from .config import config

# Load environment variables from .env file
load_dotenv()

# Create the Symptom Analysis Agent with only Google Search
symptom_agent = LlmAgent(
    name="symptom_analyzer",
    model=config.DEFAULT_MODEL,
    description=(
        "Friendly healthcare assistant with multimodal capabilities that greets patients, "
        "analyzes symptoms from both text descriptions and images, provides preliminary "
        "medical assessments, health information, and emergency guidance. Can examine "
        "visual symptoms like rashes, swelling, wounds, and other visible conditions. "
        "Uses Google Search for additional medical information when needed."
    ),
    instruction=SYMPTOM_ANALYZER_PROMPT,
    tools=[google_search],
) 