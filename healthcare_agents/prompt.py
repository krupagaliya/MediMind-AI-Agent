"""
Healthcare Agent Prompts
Contains all prompts and instructions for the healthcare agents
"""

# Main coordinator agent prompt
COORDINATOR_PROMPT = """You are a helpful healthcare coordinator managing three specialized assistants:

**Sub-Agent 1: Symptom Analyzer** (symptom_analyzer)
- Greets patients warmly and understands their concerns
- Analyzes symptoms and provides preliminary medical assessments
- Provides health information about medical conditions
- Offers emergency guidance for critical situations
- Uses Google Search for additional medical information

**Sub-Agent 2: Hospital Finder** (hospital_finder)
- Finds nearby hospitals and medical facilities
- Uses Google Places API to get accurate location data
- Provides hospital details: address, phone, rating, hours
- Locates emergency hospitals and specialists
- Calculates distances and provides directions

**Sub-Agent 3: Home Remedies Advisor** (home_remedies_advisor)
- Suggests natural, safe home remedies for light symptoms only
- Provides preparation instructions using common household items
- Offers safety guidance and knows when to refer to medical care
- Specializes in traditional remedies for mild conditions
- Uses Google Search for additional remedy information

**Your Role as Coordinator:**
1. **Determine user needs** - Understand what the user is asking for
2. **Route to appropriate agent** - Send requests to the right specialist
3. **Coordinate responses** - Combine information from all agents when needed
4. **Provide comprehensive help** - Ensure user gets complete assistance

**When to use each agent:**
- Use **symptom_analyzer** for:
  - Greeting and understanding patient concerns
  - Symptom analysis and health assessments
  - Health information about medical conditions
  - Emergency guidance and first aid instructions
  - Medical information searches

- Use **hospital_finder** for:
  - Finding nearby hospitals or medical facilities
  - Getting hospital contact information and details
  - Locating emergency hospitals
  - Finding medical specialists in specific areas
  - Getting directions to medical facilities

- Use **home_remedies_advisor** for:
  - Natural remedies for light/mild symptoms only
  - Home remedy preparation instructions
  - Traditional remedies using household items
  - Mild conditions like light headaches, minor coughs, slight nausea
  - When user specifically asks for home remedies or natural treatments

**Coordination Examples:**
- If someone has symptoms AND needs a hospital: First analyze symptoms, then find appropriate medical facilities
- If someone needs emergency help: Provide emergency guidance AND find nearest emergency hospitals
- If someone asks about a condition: Provide health information AND suggest nearby specialists
- If someone has light symptoms AND asks for home remedies: Use home_remedies_advisor for natural treatments
- If someone has mild symptoms: Offer both medical assessment AND home remedy options
- If symptoms are severe: Use symptom_analyzer and hospital_finder, avoid home remedies

**Important Guidelines:**
- Always prioritize patient safety and emergency situations
- For medical emergencies, emphasize calling 108 immediately (India Emergency Number)
- Provide comprehensive responses that address all user needs
- Be empathetic and understanding in all interactions
- Include appropriate medical disclaimers
- Coordinate between agents seamlessly for the best user experience

**Example Interactions:**
- 'Hello! I can help you with health concerns and find medical facilities. What do you need help with?'
- 'Let me analyze your symptoms and also find nearby hospitals for you.'
- 'Based on your symptoms, here's what I found. I can also locate nearby specialists if needed.'
- 'For this emergency situation, here's immediate guidance, and here are the nearest hospitals.'"""

# Symptom analyzer agent prompt
SYMPTOM_ANALYZER_PROMPT = """You are a caring and helpful healthcare assistant. Your role is to:

1. **Greet patients warmly** - Always start with a friendly greeting and ask how you can help
2. **Understand symptoms** - Listen carefully to patient descriptions and ask clarifying questions
3. **Analyze symptoms** - Provide preliminary assessments based on symptoms described
4. **Provide health information** - Give basic information about medical conditions
5. **Emergency guidance** - Provide immediate guidance for emergency situations
6. **Search for additional info** - Use Google Search when patients need more detailed medical information

When interacting with patients:
- Always be empathetic and understanding
- Ask follow-up questions to better understand their situation
- Provide clear, easy-to-understand explanations
- Always emphasize the importance of professional medical care
- For emergencies, immediately direct to call 108 (India Emergency Number)
- Use Google Search to find additional medical information when needed

IMPORTANT REMINDERS:
- Always include medical disclaimers
- Never provide definitive medical diagnoses
- Always recommend consulting healthcare professionals
- Prioritize patient safety above all else
- For urgent symptoms, emphasize immediate medical attention

Example interactions:
- 'Hello! I'm here to help with your health concerns. What symptoms are you experiencing?'
- 'I understand you're feeling unwell. Can you tell me more about your symptoms?'
- 'Based on what you've described, let me analyze your symptoms...'
- 'For more detailed information, let me search for recent medical information...'"""

# Hospital finder agent prompt
HOSPITAL_FINDER_PROMPT = """You are a helpful medical facility locator for India. Your role is to:

1. **Auto-detect location** - Automatically detect user's location using IP address
2. **Find nearby hospitals** - Locate hospitals and medical facilities in the detected area
3. **Provide facility details** - Give comprehensive information about medical facilities
4. **Emergency hospital location** - Quickly find the nearest emergency hospitals
5. **Direction assistance** - Provide hospital information and contact details

When helping users find medical facilities:
- Automatically detect their location (no need to ask for location)
- Provide comprehensive facility information (name, address, phone, rating, hours)
- For emergencies, prioritize emergency hospitals and urgent care centers
- Suggest multiple options when available
- Provide clear contact information for all facilities
- Focus on hospitals in India with local contact details

IMPORTANT REMINDERS:
- For medical emergencies, always remind users to call 108 immediately (India Emergency Number)
- Automatically detect location - no need to ask users for their location
- Provide multiple hospital options when available
- Include contact information for all facilities
- Prioritize emergency facilities for urgent situations
- Provide hospitals with Indian phone numbers and addresses

Example interactions:
- 'I've detected your location and found nearby hospitals in your area.'
- 'Let me find the nearest emergency hospitals based on your current location.'
- 'Here are the top-rated hospitals near you with their contact information.'
- 'For your emergency situation, here are the closest hospitals with directions. Remember to call 108 immediately.'"""

# # To Be Use in the Future: Emergency guidance templates
EMERGENCY_GUIDANCE = {
    "heart_attack": {
        "signs": ["Chest pain", "Shortness of breath", "Nausea", "Sweating", "Pain in arm or jaw"],
        "actions": [
            "🚨 Call 108 immediately (India Emergency Number)",
            "Help person sit down and rest",
            "Loosen tight clothing",
            "If prescribed, help with nitroglycerin",
            "Be ready to perform CPR if needed"
        ]
    },
    "stroke": {
        "signs": ["Face drooping", "Arm weakness", "Speech difficulty", "Sudden confusion"],
        "actions": [
            "🚨 Call 108 immediately (India Emergency Number)",
            "Note the time symptoms started",
            "Keep person calm and lying down",
            "Turn head to side if vomiting",
            "Stay with the person"
        ]
    },
    "choking": {
        "signs": ["Unable to speak", "Difficulty breathing", "Clutching throat", "Blue lips or face"],
        "actions": [
            "Ask 'Are you choking?'",
            "If unable to speak, perform Heimlich maneuver",
            "Call 108 if unsuccessful",
            "Continue until object dislodges or person becomes unconscious"
        ]
    },
    "severe_bleeding": {
        "signs": ["Heavy bleeding", "Deep cuts", "Bleeding that won't stop"],
        "actions": [
            "🚨 Call 108 for severe bleeding (India Emergency Number)",
            "Apply direct pressure with clean cloth",
            "Elevate injured area above heart if possible",
            "Don't remove object if embedded",
            "Keep person warm and calm"
        ]
    },
    "allergic_reaction": {
        "signs": ["Difficulty breathing", "Swelling of face/throat", "Hives", "Rapid pulse"],
        "actions": [
            "🚨 Call 108 immediately (India Emergency Number)",
            "Use EpiPen if available",
            "Help person sit upright",
            "Remove or avoid allergen",
            "Monitor breathing"
        ]
    }
}

# To Be Use in the Future: Common symptoms database
SYMPTOMS_DATABASE = {
    "fever": {
        "conditions": ["Common cold", "Flu", "Viral infection", "Bacterial infection"],
        "urgency": "moderate",
        "recommendations": ["Rest", "Stay hydrated", "Monitor temperature", "Consult doctor if fever persists over 3 days"]
    },
    "headache": {
        "conditions": ["Tension headache", "Migraine", "Dehydration", "Stress", "Eye strain"],
        "urgency": "low",
        "recommendations": ["Rest in quiet, dark room", "Stay hydrated", "Apply cold/warm compress", "Avoid bright lights"]
    },
    "chest_pain": {
        "conditions": ["Heart attack", "Angina", "Muscle strain", "Anxiety", "Acid reflux"],
        "urgency": "high",
        "recommendations": ["SEEK IMMEDIATE MEDICAL ATTENTION", "Call emergency services", "Do not drive yourself", "Stay calm"]
    },
    "shortness_of_breath": {
        "conditions": ["Asthma", "Pneumonia", "Heart problems", "Anxiety", "Allergic reaction"],
        "urgency": "high",
        "recommendations": ["SEEK IMMEDIATE MEDICAL ATTENTION", "Use inhaler if available", "Sit upright", "Stay calm"]
    },
    "cough": {
        "conditions": ["Common cold", "Bronchitis", "Allergies", "Pneumonia", "Acid reflux"],
        "urgency": "low",
        "recommendations": ["Stay hydrated", "Use honey for throat relief", "Avoid irritants", "Rest"]
    },
    "stomach_pain": {
        "conditions": ["Indigestion", "Food poisoning", "Gastritis", "Appendicitis", "Stress"],
        "urgency": "moderate",
        "recommendations": ["Rest", "Avoid solid foods temporarily", "Stay hydrated", "Monitor symptoms"]
    },
    "nausea": {
        "conditions": ["Food poisoning", "Gastritis", "Pregnancy", "Migraine", "Anxiety"],
        "urgency": "low",
        "recommendations": ["Rest", "Sip clear fluids", "Avoid strong odors", "Eat bland foods"]
    },
    "dizziness": {
        "conditions": ["Dehydration", "Low blood pressure", "Inner ear problems", "Anxiety", "Medication side effects"],
        "urgency": "moderate",
        "recommendations": ["Sit or lie down", "Stay hydrated", "Avoid sudden movements", "Rest"]
    }
}

# To Be Use in the Future: Health information database
HEALTH_INFO_DATABASE = {
    "diabetes": {
        "description": "A condition where blood sugar levels are too high",
        "symptoms": ["Increased thirst", "Frequent urination", "Fatigue", "Blurred vision"],
        "care": ["Monitor blood sugar", "Healthy diet", "Regular exercise", "Take medications as prescribed"],
        "when_to_seek_help": "If blood sugar is very high or low, or if you have severe symptoms"
    },
    "hypertension": {
        "description": "High blood pressure condition",
        "symptoms": ["Often no symptoms", "Headaches", "Shortness of breath"],
        "care": ["Limit salt intake", "Exercise regularly", "Maintain healthy weight", "Take medications as prescribed"],
        "when_to_seek_help": "For regular monitoring and if you experience severe symptoms"
    },
    "asthma": {
        "description": "Chronic condition affecting breathing",
        "symptoms": ["Wheezing", "Shortness of breath", "Chest tightness", "Coughing"],
        "care": ["Avoid triggers", "Use inhalers as prescribed", "Monitor symptoms", "Keep rescue inhaler handy"],
        "when_to_seek_help": "If breathing becomes difficult or rescue inhaler doesn't help"
    },
    "common_cold": {
        "description": "Viral infection affecting nose and throat",
        "symptoms": ["Runny nose", "Sneezing", "Cough", "Sore throat"],
        "care": ["Rest", "Stay hydrated", "Use saline nasal spray", "Throat lozenges"],
        "when_to_seek_help": "If symptoms worsen or last more than 10 days"
    },
    "flu": {
        "description": "Viral infection affecting respiratory system",
        "symptoms": ["Fever", "Body aches", "Fatigue", "Cough"],
        "care": ["Rest", "Stay hydrated", "Use fever reducers if needed", "Isolate from others"],
        "when_to_seek_help": "If breathing difficulties or high fever persists"
    }
}

# Home remedies agent prompt
HOME_REMEDIES_PROMPT = """You are a knowledgeable home remedies advisor specializing in natural, safe remedies for light symptoms. Your role is to:

1. **Assess symptom severity** - Determine if symptoms are light/mild and suitable for home remedies
2. **Suggest natural remedies** - Provide safe, effective home remedies using common household items
3. **Provide preparation instructions** - Give clear, step-by-step instructions for remedy preparation
4. **Safety guidance** - Ensure all suggestions are safe and appropriate for the user
5. **Know limitations** - Recognize when symptoms require professional medical attention

**When to suggest home remedies:**
- Light symptoms like mild headaches, minor coughs, slight nausea
- Common cold symptoms (runny nose, mild sore throat)
- Minor digestive issues (mild indigestion, bloating)
- Light skin irritations or minor cuts
- Mild stress or anxiety
- Minor muscle aches or tension

**When NOT to suggest home remedies (refer to medical care):**
- High fever (above 101°F/38.3°C)
- Severe pain or persistent symptoms
- Breathing difficulties
- Chest pain or heart-related symptoms
- Severe allergic reactions
- Symptoms lasting more than a few days
- Any emergency situations

**Home Remedy Categories:**
- **Herbal teas and drinks** (ginger tea, honey-lemon water, turmeric milk)
- **Kitchen ingredients** (garlic, honey, ginger, turmeric, salt water)
- **Essential oils and aromatherapy** (eucalyptus, peppermint, lavender)
- **Hot/cold therapy** (warm compresses, ice packs)
- **Dietary remedies** (BRAT diet, probiotics, hydration)
- **Relaxation techniques** (breathing exercises, gentle stretches)

**Important Guidelines:**
- Always emphasize that these are for LIGHT symptoms only
- Include preparation instructions and dosage guidance
- Mention any potential allergies or contraindications
- Suggest when to seek medical attention if symptoms worsen
- Include the medical disclaimer in all responses
- Focus on evidence-based, traditional remedies with good safety profiles

**Example interactions:**
- 'For your mild headache, I can suggest some gentle home remedies...'
- 'These light cold symptoms can often be helped with natural remedies...'
- 'Let me suggest some safe home remedies for your minor digestive discomfort...'
- 'Your symptoms seem mild enough for home care, but let me know if they worsen...'"""

# To Be Use in the Future: Home remedies database
HOME_REMEDIES_DATABASE = {
    "mild_headache": {
        "remedies": [
            {
                "name": "Peppermint Oil Compress",
                "ingredients": ["2-3 drops peppermint oil", "1 cup cool water", "Clean cloth"],
                "preparation": "Mix peppermint oil with water, soak cloth, apply to forehead for 10-15 minutes",
                "benefits": "Natural cooling effect, reduces tension"
            },
            {
                "name": "Ginger Tea",
                "ingredients": ["1 inch fresh ginger", "1 cup hot water", "Honey (optional)"],
                "preparation": "Steep sliced ginger in hot water for 10 minutes, add honey if desired",
                "benefits": "Anti-inflammatory properties, improves circulation"
            },
            {
                "name": "Hydration Therapy",
                "ingredients": ["Water", "Pinch of sea salt", "Lemon juice"],
                "preparation": "Drink 2-3 glasses of water with a pinch of salt and lemon",
                "benefits": "Rehydrates body, balances electrolytes"
            }
        ],
        "additional_tips": ["Rest in a dark, quiet room", "Gentle neck and shoulder massage", "Avoid screens and bright lights"]
    },
    "mild_cough": {
        "remedies": [
            {
                "name": "Honey and Warm Water",
                "ingredients": ["1-2 tablespoons honey", "1 cup warm water", "Lemon juice (optional)"],
                "preparation": "Mix honey in warm water, add lemon if desired, sip slowly",
                "benefits": "Soothes throat, natural antibacterial properties"
            },
            {
                "name": "Turmeric Milk",
                "ingredients": ["1 cup warm milk", "1/2 teaspoon turmeric powder", "Pinch of black pepper"],
                "preparation": "Mix turmeric and pepper in warm milk, drink before bedtime",
                "benefits": "Anti-inflammatory, boosts immunity"
            },
            {
                "name": "Steam Inhalation",
                "ingredients": ["Hot water", "2-3 drops eucalyptus oil (optional)"],
                "preparation": "Inhale steam from hot water for 5-10 minutes, cover head with towel",
                "benefits": "Loosens mucus, soothes airways"
            }
        ],
        "additional_tips": ["Stay hydrated", "Use a humidifier", "Avoid cold drinks", "Rest your voice"]
    },
    "mild_nausea": {
        "remedies": [
            {
                "name": "Ginger Tea",
                "ingredients": ["1 inch fresh ginger", "1 cup hot water", "Honey"],
                "preparation": "Steep ginger in hot water for 10 minutes, add honey to taste",
                "benefits": "Natural anti-nausea properties, settles stomach"
            },
            {
                "name": "Peppermint Tea",
                "ingredients": ["Fresh peppermint leaves or tea bag", "1 cup hot water"],
                "preparation": "Steep peppermint in hot water for 5-7 minutes",
                "benefits": "Calms digestive system, reduces nausea"
            },
            {
                "name": "BRAT Diet",
                "ingredients": ["Bananas", "Rice", "Applesauce", "Toast"],
                "preparation": "Eat small portions of bland foods",
                "benefits": "Easy to digest, helps settle stomach"
            }
        ],
        "additional_tips": ["Eat small, frequent meals", "Avoid strong odors", "Stay hydrated with small sips"]
    },
    "mild_sore_throat": {
        "remedies": [
            {
                "name": "Salt Water Gargle",
                "ingredients": ["1/2 teaspoon salt", "1 cup warm water"],
                "preparation": "Dissolve salt in warm water, gargle for 30 seconds, repeat 3-4 times daily",
                "benefits": "Reduces inflammation, kills bacteria"
            },
            {
                "name": "Honey and Lemon",
                "ingredients": ["1 tablespoon honey", "1 tablespoon lemon juice", "1 cup warm water"],
                "preparation": "Mix honey and lemon in warm water, sip slowly",
                "benefits": "Soothes throat, provides vitamin C"
            },
            {
                "name": "Turmeric Gargle",
                "ingredients": ["1/2 teaspoon turmeric", "1/2 teaspoon salt", "1 cup warm water"],
                "preparation": "Mix ingredients, gargle for 30 seconds, repeat twice daily",
                "benefits": "Anti-inflammatory and antimicrobial properties"
            }
        ],
        "additional_tips": ["Stay hydrated", "Use a humidifier", "Avoid irritants like smoke"]
    },
    "mild_indigestion": {
        "remedies": [
            {
                "name": "Fennel Seed Tea",
                "ingredients": ["1 teaspoon fennel seeds", "1 cup hot water"],
                "preparation": "Steep fennel seeds in hot water for 10 minutes, strain and drink",
                "benefits": "Aids digestion, reduces bloating"
            },
            {
                "name": "Ajwain (Carom Seeds) Water",
                "ingredients": ["1 teaspoon ajwain", "1 cup warm water"],
                "preparation": "Soak ajwain in warm water for 10 minutes, strain and drink",
                "benefits": "Improves digestion, reduces gas"
            },
            {
                "name": "Lemon and Baking Soda",
                "ingredients": ["1 tablespoon lemon juice", "1/2 teaspoon baking soda", "1 cup water"],
                "preparation": "Mix ingredients, drink slowly when fizzing stops",
                "benefits": "Neutralizes stomach acid, aids digestion"
            }
        ],
        "additional_tips": ["Eat smaller meals", "Avoid spicy foods", "Take a gentle walk after eating"]
    },
    "minor_stress": {
        "remedies": [
            {
                "name": "Chamomile Tea",
                "ingredients": ["1 chamomile tea bag or 1 tsp dried chamomile", "1 cup hot water", "Honey (optional)"],
                "preparation": "Steep chamomile in hot water for 5-7 minutes, add honey if desired",
                "benefits": "Natural relaxant, promotes calm"
            },
            {
                "name": "Lavender Aromatherapy",
                "ingredients": ["2-3 drops lavender essential oil", "Diffuser or tissue"],
                "preparation": "Add oil to diffuser or inhale from tissue for 5-10 minutes",
                "benefits": "Reduces anxiety, promotes relaxation"
            },
            {
                "name": "Deep Breathing Exercise",
                "ingredients": ["Just yourself and a quiet space"],
                "preparation": "Breathe in for 4 counts, hold for 4, exhale for 6, repeat 10 times",
                "benefits": "Activates relaxation response, reduces stress hormones"
            }
        ],
        "additional_tips": ["Practice regular meditation", "Get adequate sleep", "Exercise regularly", "Limit caffeine"]
    }
}

# Medical disclaimer
MEDICAL_DISCLAIMER = """
⚠️ MEDICAL DISCLAIMER: This information is for educational purposes only and should not replace professional medical advice. Always consult with healthcare professionals for proper diagnosis and treatment. For medical emergencies, call 108 immediately (India Emergency Number).
""" 