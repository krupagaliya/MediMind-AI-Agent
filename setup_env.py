#!/usr/bin/env python3
"""
Environment Setup Script for Healthcare Agent System
This script helps you create a .env file with the necessary environment variables.
"""

import os
import sys

def create_env_file():
    """Create a .env file with all necessary environment variables"""
    
    env_template = """# Google AI API Configuration
GOOGLE_API_KEY=your_google_ai_api_key_here
GOOGLE_GENAI_USE_VERTEXAI=False

# Google Places API Configuration
GOOGLE_PLACES_API_KEY=your_google_places_api_key_here

# Google Cloud Configuration (if using Vertex AI)
GOOGLE_CLOUD_PROJECT=your_project_id
GOOGLE_CLOUD_LOCATION=us-central1
GOOGLE_APPLICATION_CREDENTIALS=path/to/your/service-account-key.json

# Application Configuration
LOG_LEVEL=INFO
DEBUG_MODE=False
MAX_SEARCH_RESULTS=10
CACHE_TIMEOUT=3600

# Security Configuration
ENABLE_RATE_LIMITING=True
MAX_REQUESTS_PER_MINUTE=60
ENABLE_AUDIT_LOG=True

# Healthcare-specific Configuration
DEFAULT_MODEL=gemini-2.0-flash
MODEL_TEMPERATURE=0.7
MODEL_MAX_TOKENS=2048

# Emergency Contact Information
EMERGENCY_SERVICES=911
POISON_CONTROL=1-800-222-1222
SUICIDE_PREVENTION=988
MENTAL_HEALTH_CRISIS=1-800-985-5990
"""

    env_file_path = ".env"
    
    # Check if .env file already exists
    if os.path.exists(env_file_path):
        response = input(f"⚠️  {env_file_path} already exists. Do you want to overwrite it? (y/N): ")
        if response.lower() not in ['y', 'yes']:
            print("❌ Setup cancelled. Existing .env file preserved.")
            return False
    
    try:
        # Write the .env file
        with open(env_file_path, 'w') as f:
            f.write(env_template)
        
        print(f"✅ {env_file_path} file created successfully!")
        print("\n📝 Next steps:")
        print("1. Edit the .env file and replace the placeholder values:")
        print("   - GOOGLE_API_KEY: Get from https://aistudio.google.com/")
        print("   - GOOGLE_PLACES_API_KEY: Get from https://console.cloud.google.com/")
        print("\n2. Required API keys:")
        print("   🔑 GOOGLE_API_KEY - Required for AI responses")
        print("   🗺️  GOOGLE_PLACES_API_KEY - Required for hospital search")
        print("\n3. After setting up your API keys, run:")
        print("   pip install -r requirements.txt")
        print("   adk web")
        
        return True
        
    except Exception as e:
        print(f"❌ Error creating {env_file_path}: {str(e)}")
        return False

def validate_env_file():
    """Validate the .env file and check for required variables"""
    
    env_file_path = ".env"
    
    if not os.path.exists(env_file_path):
        print(f"❌ {env_file_path} file not found!")
        print("Run this script first to create the .env file.")
        return False
    
    required_vars = {
        'GOOGLE_API_KEY': 'Google AI API key',
        'GOOGLE_PLACES_API_KEY': 'Google Places API key'
    }
    
    vertex_ai_vars = {
        'GOOGLE_CLOUD_PROJECT': 'Google Cloud project ID',
        'GOOGLE_APPLICATION_CREDENTIALS': 'Path to service account JSON file'
    }
    
    missing_vars = []
    placeholder_vars = []
    vertex_ai_enabled = False
    
    try:
        with open(env_file_path, 'r') as f:
            content = f.read()
            
        # Check if Vertex AI is enabled
        if "GOOGLE_GENAI_USE_VERTEXAI=True" in content:
            vertex_ai_enabled = True
            
        for var_name, description in required_vars.items():
            if f"{var_name}=" not in content:
                missing_vars.append(f"{var_name} ({description})")
            elif f"{var_name}=your_" in content:
                placeholder_vars.append(f"{var_name} ({description})")
        
        # Check Vertex AI specific variables if enabled
        if vertex_ai_enabled:
            for var_name, description in vertex_ai_vars.items():
                if f"{var_name}=" not in content:
                    missing_vars.append(f"{var_name} ({description}) - Required for Vertex AI")
                elif f"{var_name}=your_" in content or f"{var_name}=path/to/" in content:
                    placeholder_vars.append(f"{var_name} ({description}) - Required for Vertex AI")
    
        if missing_vars:
            print("❌ Missing required environment variables:")
            for var in missing_vars:
                print(f"   - {var}")
        
        if placeholder_vars:
            print("⚠️  Environment variables with placeholder values:")
            for var in placeholder_vars:
                print(f"   - {var}")
            print("\n📝 Please update these with your actual API keys.")
        
        if not missing_vars and not placeholder_vars:
            print("✅ Environment variables look good!")
            if vertex_ai_enabled:
                print("🔧 Vertex AI is enabled - make sure your service account JSON file exists at the specified path.")
            return True
        else:
            print(f"\n📝 Edit {env_file_path} and replace placeholder values with your actual API keys.")
            if vertex_ai_enabled:
                print("🔧 Note: Vertex AI is enabled, make sure to provide valid Google Cloud credentials.")
            return False
            
    except Exception as e:
        print(f"❌ Error reading {env_file_path}: {str(e)}")
        return False

def show_api_key_instructions():
    """Show detailed instructions for obtaining API keys"""
    
    print("\n" + "="*60)
    print("📚 How to Get Your API Keys")
    print("="*60)
    
    print("\n🔑 Google AI API Key (GOOGLE_API_KEY):")
    print("1. Go to https://aistudio.google.com/")
    print("2. Sign in with your Google account")
    print("3. Click 'Get API key' or 'Create API key'")
    print("4. Copy the generated API key")
    print("5. Paste it in your .env file as: GOOGLE_API_KEY=your_actual_api_key")
    
    print("\n🗺️  Google Places API Key (GOOGLE_PLACES_API_KEY):")
    print("1. Go to https://console.cloud.google.com/")
    print("2. Create a new project or select existing project")
    print("3. Enable the 'Places API' and 'Geocoding API'")
    print("4. Go to 'Credentials' and create an API key")
    print("5. Copy the API key")
    print("6. Paste it in your .env file as: GOOGLE_PLACES_API_KEY=your_actual_api_key")
    
    print("\n🔒 Google Cloud Service Account (for Vertex AI):")
    print("1. Go to https://console.cloud.google.com/")
    print("2. Navigate to 'IAM & Admin' > 'Service Accounts'")
    print("3. Create a new service account or use existing one")
    print("4. Add roles: 'Vertex AI User' and 'AI Platform Developer'")
    print("5. Create and download the JSON key file")
    print("6. Save the JSON file in your project directory")
    print("7. Update .env file: GOOGLE_APPLICATION_CREDENTIALS=path/to/your/service-account-key.json")
    
    print("\n💡 Pro Tips:")
    print("- Keep your API keys secure and never share them publicly")
    print("- Consider setting usage limits on your API keys")
    print("- The Google AI API key is usually free for moderate usage")
    print("- Google Places API may require billing setup after free tier")
    print("- For Vertex AI: Set GOOGLE_GENAI_USE_VERTEXAI=True in .env")
    print("- For AI Studio: Set GOOGLE_GENAI_USE_VERTEXAI=False in .env")
    print("- Service account JSON files should never be committed to version control")

def main():
    """Main function"""
    
    print("🏥 Healthcare Agent System - Environment Setup")
    print("="*50)
    
    if len(sys.argv) > 1 and sys.argv[1] == "--validate":
        validate_env_file()
        return
    
    if len(sys.argv) > 1 and sys.argv[1] == "--help":
        show_api_key_instructions()
        return
    
    print("\nThis script will help you set up the environment variables for the healthcare agent system.")
    print("You'll need API keys from Google AI Studio and Google Cloud Platform.")
    
    # Create .env file
    if create_env_file():
        print("\n" + "-"*50)
        validate_env_file()
        
        print("\n💡 Need help getting API keys? Run:")
        print("   python setup_env.py --help")
        
        print("\n🔍 To validate your .env file later, run:")
        print("   python setup_env.py --validate")

if __name__ == "__main__":
    main() 