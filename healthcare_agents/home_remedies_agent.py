"""
Agent 3: Home Remedies Agent
Clean and simple agent that suggests natural remedies for light symptoms
All prompts are stored in prompt.py
"""

import os
from dotenv import load_dotenv
from google.adk.agents import LlmAgent
from google.adk.tools import google_search
from .prompt import HOME_REMEDIES_PROMPT

# Load environment variables from .env file
load_dotenv()

# Create the Home Remedies Agent with Google Search for additional remedy information
home_remedies_agent = LlmAgent(
    name="home_remedies_advisor",
    model="gemini-2.0-flash",
    description=(
        "Knowledgeable home remedies advisor that suggests natural, safe remedies "
        "for light symptoms using common household items. Provides preparation "
        "instructions and safety guidance for mild conditions only."
    ),
    instruction=HOME_REMEDIES_PROMPT,
    tools=[google_search],
)
