"""Deployment script for Healthcare Agent System."""

import asyncio
import os
import sys
from dotenv import load_dotenv

from healthcare_agents.agent import root_agent
from google.adk.sessions import VertexAiSessionService

import vertexai
from vertexai import agent_engines
from vertexai.preview.reasoning_engines import AdkApp


def load_deployment_config():
    """Load deployment configuration from .env1 file."""
    # Load from .env1 file
    env1_path = ".env1"
    if not os.path.exists(env1_path):
        print(f"❌ {env1_path} file not found!")
        print("Please create a .env1 file with your deployment configuration.")
        return None
    
    load_dotenv(env1_path)
    
    config = {
        "project_id": os.getenv("GOOGLE_CLOUD_PROJECT"),
        "location": os.getenv("GOOGLE_CLOUD_LOCATION", "us-central1"),
        "bucket": os.getenv("GOOGLE_CLOUD_STORAGE_BUCKET"),
        "google_places_api_key": os.getenv("GOOGLE_PLACES_API_KEY"),
        "google_api_key": os.getenv("GOOGLE_API_KEY"),
        "deployment_name": os.getenv("DEPLOYMENT_NAME", "Healthcare-Agent-ADK"),
        "deployment_description": os.getenv("DEPLOYMENT_DESCRIPTION", "Healthcare Agent System with symptom analysis and hospital finder"),
    }
    
    return config


def validate_config(config):
    """Validate required configuration values."""
    required_vars = [
        "project_id",
        "location", 
        "bucket",
        "google_places_api_key"
    ]
    
    missing_vars = []
    for var in required_vars:
        if not config.get(var):
            missing_vars.append(var)
    
    if missing_vars:
        print("❌ Missing required environment variables in .env1:")
        for var in missing_vars:
            print(f"   - {var.upper()}")
        return False
    
    return True


def create_deployment(config):
    """Creates a new deployment."""
    print("🚀 Creating new healthcare agent deployment...")
    
    # Prepare environment variables for the deployment
    env_vars = {
        "GOOGLE_PLACES_API_KEY": config["google_places_api_key"],
    }
    
    # Add Google API key if provided (for AI Studio)
    if config.get("google_api_key"):
        env_vars["GOOGLE_API_KEY"] = config["google_api_key"]
    
    print(f"📋 Environment variables: {list(env_vars.keys())}")
    
    app = AdkApp(
        agent=root_agent,
        enable_tracing=True,
        env_vars=env_vars,
    )

    remote_agent = agent_engines.create(
        app,
        display_name=config["deployment_name"],
        description=config["deployment_description"],
        requirements=[
            "google-adk>=1.0.0",
            "google-cloud-aiplatform[agent_engines]>=1.93.1",
            "google-genai>=1.16.1",
            "pydantic>=2.10.6,<3.0.0",
            "requests>=2.32.3,<3.0.0",
            "python-dotenv>=1.0.0",
        ],
        extra_packages=[
            "./healthcare_agents",  # The main package
        ],
    )
    print(f"✅ Created remote agent: {remote_agent.resource_name}")
    print(f"📋 Resource ID: {remote_agent.resource_name.split('/')[-1]}")
    return remote_agent.resource_name


def delete_deployment(resource_id):
    """Deletes an existing deployment."""
    print(f"🗑️  Deleting deployment: {resource_id}")
    remote_agent = agent_engines.get(resource_id)
    remote_agent.delete(force=True)
    print(f"✅ Deleted remote agent: {resource_id}")


def test_deployment(config, resource_id):
    """Test the deployed agent with a sample query."""
    print(f"🧪 Testing deployment: {resource_id}")
    
    session_service = VertexAiSessionService(config["project_id"], config["location"])
    
    session = asyncio.run(session_service.create_session(
            app_name=resource_id,
            user_id="healthcare_user_test"
        )
    )

    remote_agent = agent_engines.get(resource_id)
    
    # Test with a healthcare-specific query
    test_message = "I have a fever and headache. Can you help me find nearby hospitals?"
    
    print(f"📤 Sending test message: {test_message}")
    print("📥 Response:")
    
    for event in remote_agent.stream_query(
        user_id="healthcare_user_test",
        session_id=session.id,
        message=test_message,
    ):
        print(event)
    
    print("✅ Test completed.")


def main():
    """Main function to handle deployment operations."""
    print("🏥 Healthcare Agent Deployment System")
    print("=" * 50)
    
    # Load configuration from .env1
    config = load_deployment_config()
    if not config:
        return
    
    # Validate configuration
    if not validate_config(config):
        return
    
    # Display configuration
    print(f"📋 Configuration:")
    print(f"   Project ID: {config['project_id']}")
    print(f"   Location: {config['location']}")
    print(f"   Bucket: {config['bucket']}")
    print(f"   Deployment Name: {config['deployment_name']}")
    print()
    
    # Initialize Vertex AI
    vertexai.init(
        project=config["project_id"],
        location=config["location"],
        staging_bucket=f"gs://{config['bucket']}",
    )
    
    # Get command from command line arguments
    if len(sys.argv) < 2:
        print("❌ Please specify a command:")
        print("   python deploy.py create")
        print("   python deploy.py delete <resource_id>")
        print("   python deploy.py test <resource_id>")
        return
    
    command = sys.argv[1].lower()
    
    if command == "create":
        resource_name = create_deployment(config)
        print(f"\n🎉 Deployment successful!")
        print(f"💡 To test: python deploy.py test {resource_name.split('/')[-1]}")
        print(f"💡 To delete: python deploy.py delete {resource_name.split('/')[-1]}")
        
    elif command == "delete":
        if len(sys.argv) < 3:
            print("❌ Please provide resource_id for delete command")
            print("   python deploy.py delete <resource_id>")
            return
        
        resource_id = sys.argv[2]
        delete_deployment(resource_id)
        
    elif command == "test":
        if len(sys.argv) < 3:
            print("❌ Please provide resource_id for test command")
            print("   python deploy.py test <resource_id>")
            return
        
        resource_id = sys.argv[2]
        test_deployment(config, resource_id)
        
    else:
        print(f"❌ Unknown command: {command}")
        print("Available commands: create, delete, test")


if __name__ == "__main__":
    main()
