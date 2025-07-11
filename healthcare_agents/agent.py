"""
Main Healthcare Agent - Coordinator
Coordinates between two specialized sub-agents:
1. Symptom Analyzer Agent - Handles symptoms, health info, emergency guidance
2. Hospital Finder Agent - Finds nearby hospitals using Google Places API
"""


from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

# Load environment variables from .env file
load_dotenv()

# Import prompts from prompt.py
from .prompt import COORDINATOR_PROMPT

# Import the two sub-agents
from healthcare_agents.symptom_agent import symptom_agent
from healthcare_agents.hospital_finder_agent import hospital_finder_agent

# Wrap the sub-agents as tools with output_key for symptom_agent
symptom_analyzer_tool = AgentTool(agent=symptom_agent)
hospital_finder_tool = AgentTool(agent=hospital_finder_agent)

# Create the main coordinator agent
root_agent = Agent(
    name="healthcare_coordinator",
    model="gemini-2.0-flash",
    # model="gemini-2.0-flash-live-001",
    description=(
        "Main healthcare coordinator that manages two specialized sub-agents: "
        "a symptom analyzer for health assessments and a hospital finder for location services."
    ),
    instruction=COORDINATOR_PROMPT,
    tools=[
        symptom_analyzer_tool,
        hospital_finder_tool
    ],
) 