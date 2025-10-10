"""
Main Healthcare Agent - Coordinator
Coordinates between three specialized sub-agents:
1. Symptom Analyzer Agent - Handles symptoms, health info, emergency guidance
2. Hospital Finder Agent - Finds nearby hospitals using Google Places API
3. Home Remedies Agent - Suggests natural remedies for light symptoms
"""


from dotenv import load_dotenv
from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

# Load environment variables from .env file
load_dotenv()

# Import prompts from prompt.py
from .prompt import COORDINATOR_PROMPT

# Import the three sub-agents
from healthcare_agents.symptom_agent import symptom_agent
from healthcare_agents.hospital_finder_agent import hospital_finder_agent
from healthcare_agents.home_remedies_agent import home_remedies_agent

# Wrap the sub-agents as tools
symptom_analyzer_tool = AgentTool(agent=symptom_agent)
hospital_finder_tool = AgentTool(agent=hospital_finder_agent)
home_remedies_tool = AgentTool(agent=home_remedies_agent)

# Basic LLM Agent
# Create the main coordinator agent
root_agent = LlmAgent(
    name="healthcare_coordinator",
    model="gemini-2.5-flash",
    # model="gemini-2.0-flash-live-001", # Enable for voice mode.
    description=(
        "Main healthcare coordinator that manages three specialized sub-agents: "
        "a symptom analyzer for health assessments, a hospital finder for location services, "
        "and a home remedies advisor for natural treatments of light symptoms."
    ),
    instruction=COORDINATOR_PROMPT,
    tools=[
        symptom_analyzer_tool,
        hospital_finder_tool,
        home_remedies_tool
    ],
)


# Loop Agent which will run the sub-agents in a loop (for coordination or multi-step reasoning).
# from google.adk.agents import LoopAgent
#
# root_agent = LoopAgent(
#     name='healthcare_coordinator',
#     description=(
#         "Main healthcare coordinator that manages three specialized sub-agents: "
#                 "a symptom analyzer for health assessments, a hospital finder for location services, "
#                 "and a home remedies advisor for natural treatments of light symptoms."
#     ),
#     max_iterations=2,
#     sub_agents=[symptom_agent, home_remedies_agent, hospital_finder_agent],
# )

