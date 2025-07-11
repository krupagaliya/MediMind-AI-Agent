"""
Agent 1: Symptom Analysis Agent
Clean and simple agent that only uses Google Search for medical information
All prompts are stored in prompt.py
"""

import os
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.tools import google_search
from .prompt import SYMPTOM_ANALYZER_PROMPT

# Load environment variables from .env file
load_dotenv()

# Create the Symptom Analysis Agent with only Google Search
symptom_agent = Agent(
    name="symptom_analyzer",
    model="gemini-2.0-flash",
    description=(
        "Friendly healthcare assistant that greets patients, understands symptoms, "
        "provides symptom analysis, health information, and emergency guidance. "
        "Uses Google Search for medical information when needed."
    ),
    instruction=SYMPTOM_ANALYZER_PROMPT,
    tools=[google_search],
) 