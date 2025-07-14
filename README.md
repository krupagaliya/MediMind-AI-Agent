# Healthcare Agent System - ADK Implementation

A specialized healthcare assistant system built using Google's Agent Development Kit (ADK) framework featuring intelligent symptom analysis and hospital location services for India.

## 🏥 Overview

This healthcare agent system features a **coordinator agent** that manages two specialized sub-agents:

### 🩺 Agent 1: Symptom Analyzer
- **Friendly Patient Interaction**: Warmly greets patients and understands their health concerns
- **Symptom Analysis**: Provides preliminary assessment of symptoms with appropriate recommendations
- **Health Information**: Delivers information about medical conditions and treatments
- **Emergency Guidance**: Offers critical emergency medical guidance and instructions
- **Google Search Integration**: Uses Google Search for additional medical information

### 🏥 Agent 2: Hospital Finder
- **Auto-Location Detection**: Automatically detects user location via IP address
- **Hospital Location**: Finds nearby hospitals and medical facilities using Google Places API
- **Comprehensive Details**: Provides hospital information including address, phone, rating, and hours
- **Emergency Hospitals**: Locates emergency hospitals and urgent care centers
- **India-Focused**: Optimized for Indian healthcare system with local emergency numbers

## 🚀 Features

### Coordinator Agent Capabilities

1. **Smart Request Routing**
   - Analyzes user requests and routes to appropriate sub-agent
   - Coordinates responses from multiple agents
   - Provides comprehensive assistance

2. **Seamless Integration**
   - Combines symptom analysis with hospital location services
   - Provides emergency guidance with nearby hospital information
   - Offers health information with specialist recommendations

### Current Implementation Features

- **Automatic Location Detection**: No need to ask users for their location
- **India Emergency Integration**: Uses 108 emergency number
- **Real-time Hospital Search**: Live data from Google Places API
- **Medical Information Search**: Google Search integration for medical queries
- **Safety-First Approach**: Prioritizes emergency situations and professional medical care

## 🛠️ Installation

### Prerequisites

- Python 3.9 or higher
- Google AI Studio API key
- Google Places API key
- Internet connection for API access

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd agent-demo-health
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   **Option A: Use the setup script (Recommended)**
   ```bash
   python setup_env.py
   ```
   This will create a `.env` file with all necessary variables. Then edit the `.env` file to add your API keys.

   **Option B: Manual setup**
   Create a `.env` file in the root directory:
   ```env
   # For Google AI Studio (default)
   GOOGLE_API_KEY=your_google_ai_api_key_here
   GOOGLE_GENAI_USE_VERTEXAI=False
   
   # For Vertex AI (alternative)
   GOOGLE_GENAI_USE_VERTEXAI=True
   GOOGLE_CLOUD_PROJECT=your_project_id
   GOOGLE_CLOUD_LOCATION=us-central1
   GOOGLE_APPLICATION_CREDENTIALS=path/to/your/service-account-key.json
   
   # Required for both
   GOOGLE_PLACES_API_KEY=your_google_places_api_key_here
   DEFAULT_MODEL=gemini-2.0-flash
   ```

4. **Get your API keys**
   ```bash
   # For detailed instructions on getting API keys
   python setup_env.py --help
   ```
   
   **Required API Keys & Authentication:**
   
   **Option A: Google AI Studio (Recommended for beginners)**
   - **Google AI API Key**: Get from [Google AI Studio](https://aistudio.google.com/)
   - Set `GOOGLE_GENAI_USE_VERTEXAI=False` in `.env`
   
   **Option B: Vertex AI (Enterprise/Production)**
   - **Google Cloud Project**: Create project in [Google Cloud Console](https://console.cloud.google.com/)
   - **Service Account**: Create service account with Vertex AI permissions
   - **Service Account Key**: Download JSON key file
   - Set `GOOGLE_GENAI_USE_VERTEXAI=True` in `.env`
   - Set `GOOGLE_APPLICATION_CREDENTIALS=path/to/your/service-account-key.json`
   
   **Both options require:**
   - **Google Places API Key**: Get from [Google Cloud Console](https://console.cloud.google.com/)


5. **Validate your setup**
   ```bash
   python setup_env.py --validate
   ```

6. **Choose your AI service**
   Edit your `.env` file to select either:
   - **Google AI Studio**: Set `GOOGLE_GENAI_USE_VERTEXAI=False` (default)
   - **Vertex AI**: Set `GOOGLE_GENAI_USE_VERTEXAI=True` (enterprise)

7. **Run the agent**
   ```bash
   adk web
   ```

## 🚀 Deployment to Google Cloud vertex AI Engine.

For production deployment to Google Cloud Vertex AI, see the [Deployment Guide](deploy_guide.md).

### Quick Deployment

1. **Create deployment configuration:**
   ```bash
   cp .env1.template .env1
   # Edit .env1 with your Google Cloud settings
   ```

2. **Deploy to Vertex AI:**
   ```bash
   python deploy.py create
   ```

3. **Test deployment:**
   ```bash
   python deploy.py test <resource_id>
   ```

For detailed instructions, troubleshooting, and best practices, see [deploy_guide.md](deploy_guide.md).

## 📋 Usage Examples

### Basic Interactions

The system provides a web interface where users can interact with the healthcare coordinator:

1. **Symptom Analysis**
   - User: "I have a fever and headache"
   - System: Analyzes symptoms, provides preliminary assessment, and offers recommendations

2. **Hospital Finding**
   - User: "Find nearby hospitals"
   - System: Auto-detects location and provides list of nearby hospitals with details

3. **Emergency Guidance**
   - User: "Someone is having chest pain"
   - System: Provides immediate emergency guidance AND finds nearest emergency hospitals

4. **Health Information**
   - User: "Tell me about diabetes"
   - System: Provides comprehensive information about diabetes and management

### System Responses Include

- **Symptom Analysis**: Preliminary assessment with urgency levels
- **Hospital Information**: Name, address, phone, rating, hours, and status
- **Emergency Guidance**: Step-by-step instructions for emergency situations
- **Health Information**: Condition descriptions, symptoms, and care recommendations
- **Safety Reminders**: Always includes medical disclaimers and emergency number (108)

## 🔧 Configuration

The system uses a `.env` file for configuration loaded automatically using `python-dotenv`.

### Required Environment Variables

**Always Required:**
- `GOOGLE_PLACES_API_KEY`: Your Google Places API key (required)

**For Google AI Studio:**
- `GOOGLE_API_KEY`: Your Google AI API key (required)
- `GOOGLE_GENAI_USE_VERTEXAI`: Set to `False`

**For Vertex AI:**
- `GOOGLE_GENAI_USE_VERTEXAI`: Set to `True`
- `GOOGLE_CLOUD_PROJECT`: Your Google Cloud project ID (required)
- `GOOGLE_APPLICATION_CREDENTIALS`: Path to service account JSON file (required)

### Optional Configuration

**For Google AI Studio (default):**
- `GOOGLE_GENAI_USE_VERTEXAI`: Set to `False` (default)
- `DEFAULT_MODEL`: AI model to use (default: gemini-2.0-flash)

**For Vertex AI:**
- `GOOGLE_GENAI_USE_VERTEXAI`: Set to `True`
- `GOOGLE_CLOUD_PROJECT`: Your Google Cloud project ID (required)
- `GOOGLE_CLOUD_LOCATION`: Location for Vertex AI (default: us-central1)
- `GOOGLE_APPLICATION_CREDENTIALS`: Path to service account JSON file (required)
- `DEFAULT_MODEL`: AI model to use (default: gemini-2.0-flash)

### Example Configurations

**Google AI Studio Setup (.env file):**
```env
GOOGLE_API_KEY=your_actual_api_key_here
GOOGLE_GENAI_USE_VERTEXAI=False
GOOGLE_PLACES_API_KEY=your_places_api_key_here
DEFAULT_MODEL=gemini-2.0-flash
```

**Vertex AI Setup (.env file):**
```env
GOOGLE_GENAI_USE_VERTEXAI=True
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=us-central1
GOOGLE_APPLICATION_CREDENTIALS=./path/to/your-service-account-key.json
GOOGLE_PLACES_API_KEY=your_places_api_key_here
DEFAULT_MODEL=gemini-2.0-flash
```

### Setup Helper Commands

```bash
# Create .env file with all variables
python setup_env.py

# Get help on obtaining API keys
python setup_env.py --help

# Validate your .env file configuration
python setup_env.py --validate
```

## 🏗️ Architecture

### Project Structure

```
agent-demo-health/
├── healthcare_agents/
│   ├── __init__.py              # Package initialization
│   ├── agent.py                 # Main coordinator agent
│   ├── config.py                # Configuration management
│   ├── prompt.py                # All agent prompts and instructions
│   ├── symptom_agent.py         # Symptom analyzer agent
│   └── hospital_finder_agent.py # Hospital finder agent
├── setup_env.py                 # Environment setup script
├── deploy.py                    # Deployment script for Vertex AI
├── deploy_guide.md              # Comprehensive deployment guide
├── requirements.txt             # Python dependencies
├── LICENSE                      # MIT licence
├── Agent_demo_colab.ipynb       # Notebook to run the agent in Google Colab.
├── .env                         # Environment variables (created by setup)
├── .env1.template               # Template for deployment configuration
└── README.md                    # This file
```

### Agent Components

1. **Coordinator Agent** (`healthcare_coordinator`)
   - Routes requests to appropriate sub-agents
   - Manages multi-agent interactions
   - Provides comprehensive responses

2. **Symptom Analyzer** (`symptom_analyzer`)
   - Google Search integration for medical information
   - Symptom analysis with urgency assessment
   - Emergency guidance system

3. **Hospital Finder** (`hospital_finder`)
   - Auto-location detection via IP address
   - Google Places API integration
   - Real-time hospital information retrieval

### Key Technologies

- **Google ADK**: Agent Development Kit framework
- **Google AI (Gemini)**: Language model for agent responses
- **Google Places API**: Hospital and medical facility data
- **Google Search**: Medical information retrieval
- **Python-dotenv**: Environment variable management

## 🔒 Safety and Disclaimers

### Medical Disclaimer

**IMPORTANT**: This healthcare assistant provides general health information and should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.

### Emergency Situations

In case of medical emergency, call emergency services immediately:
- **India Emergency Services**: 108
- **Additional Emergency Numbers**: Available in system responses

### Data Privacy

- No personal health information is stored permanently
- All interactions are processed in real-time
- Location detection is automatic and temporary
- API calls are secured with proper authentication
- Service account credentials are kept local and secure
- Vertex AI provides additional enterprise security features

## 🧪 Testing

### Interactive Testing

Use the ADK web interface for testing:

```bash
adk web
```

Navigate to `http://localhost:8000` to access the web interface.

### Test Scenarios

1. **Symptom Analysis**: Test with various symptom combinations
2. **Hospital Search**: Verify location detection and hospital results
3. **Emergency Situations**: Test emergency guidance responses
4. **Health Information**: Query various medical conditions

## 🤝 Contributing

### Development Setup

1. Fork the repository
2. Create a feature branch
3. Install development dependencies
4. Test your changes
5. Submit a pull request

### Code Standards

- Follow PEP 8 style guidelines
- Include comprehensive docstrings
- Keep prompts in `prompt.py` for centralized management
- Maintain minimal agent files with only tool integration

## 📚 API Requirements

### Google AI Services

**Google AI Studio API (Option A)**
- Used for agent language model capabilities
- Free tier available for moderate usage
- Easier setup for development and testing
- Required when `GOOGLE_GENAI_USE_VERTEXAI=False`

**Vertex AI (Option B)**
- Google Cloud's enterprise AI platform
- More advanced features and enterprise support
- Requires Google Cloud project and service account
- Better for production deployments
- Required when `GOOGLE_GENAI_USE_VERTEXAI=True`

### Google Places API
- Used for hospital and medical facility search
- Requires billing setup after free tier
- Essential for hospital finder functionality
- Required for both AI Studio and Vertex AI setups


## 🌟 Future Enhancements

### Planned Features

1. **Enhanced Medical Information**
   - More comprehensive symptom database
   - Drug interaction information
   - Preventive care recommendations

2. **Improved Location Services**
   - Manual location input option
   - Multi-city hospital search
   - Specialist finder by specialty

3. **User Experience**
   - Multi-language support
   - Voice interaction capabilities
   - Mobile-optimized interface

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.


---

**Remember**: This is a healthcare information tool, not a replacement for professional medical advice. Always consult with qualified healthcare providers for medical decisions. 