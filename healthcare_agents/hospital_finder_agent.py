"""
Agent 2: Hospital Finder Agent
Clean and simple agent that finds nearby hospitals using Google Places API
Automatically detects user location via IP address
All prompts are stored in prompt.py
"""

import os
import requests
import json
from typing import List, Any, Optional, Tuple
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from .prompt import HOSPITAL_FINDER_PROMPT

# Load environment variables from .env file
load_dotenv()

def get_location_from_ip() -> Tuple[Optional[float], Optional[float], Optional[str]]:
    """Auto-detect user location via IP address."""
    try:
        ipinfo_resp = requests.get("https://ipinfo.io/json", timeout=10)
        ipinfo_resp.raise_for_status()
        data = ipinfo_resp.json()
        
        loc = data.get("loc", "")  # format: "lat,long"
        if loc:
            latitude, longitude = map(float, loc.split(","))
            city = data.get("city", "Unknown City")
            region = data.get("region", "Unknown Region")
            location_str = f"{city}, {region}"
            return latitude, longitude, location_str
            
    except Exception as e:
        print(f"Failed to auto-detect location: {e}")
        
    return None, None, None

def find_nearby_hospitals(radius: int = 5000) -> str:
    """
    Find nearby hospitals using Google Places API with auto-detected location.
    
    Args:
        radius (int): Search radius in meters (default: 5000m = 5km)
        
    Returns:
        str: Formatted list of nearby hospitals with details
    """
    try:
        # Auto-detect user location
        lat, lng, location_str = get_location_from_ip()
        
        if not lat or not lng:
            return "❌ Could not detect your location automatically. Please check your internet connection."
        
        # Get Google Places API key from environment
        api_key = os.getenv("GOOGLE_PLACES_API_KEY")
        if not api_key:
            return "❌ Google Places API key not found. Please set GOOGLE_PLACES_API_KEY environment variable."
        
        # Search for hospitals using Places API
        places_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        places_params = {
            "location": f"{lat},{lng}",
            "radius": radius,
            "type": "hospital",
            "key": api_key
        }
        
        places_response = requests.get(places_url, params=places_params)
        places_data = places_response.json()
        
        if places_data["status"] != "OK":
            return f"❌ Google Places API error: {places_data.get('status', 'Unknown error')}"
        
        # Process the results and format as readable text
        hospitals = []
        for i, place in enumerate(places_data["results"][:10], 1):  # Limit to 10 results
            
            # Get additional details for each hospital
            place_id = place.get("place_id")
            if place_id:
                details_url = "https://maps.googleapis.com/maps/api/place/details/json"
                details_params = {
                    "place_id": place_id,
                    "fields": "name,formatted_address,formatted_phone_number,rating,opening_hours,website",
                    "key": api_key
                }
                
                details_response = requests.get(details_url, params=details_params)
                details_data = details_response.json()
                
                if details_data["status"] == "OK":
                    hospital_info = details_data["result"]
                    
                    # Format hospital information as readable text
                    hospital_text = f"""
🏥 **{i}. {hospital_info.get("name", "Unknown Hospital")}**
📍 **Address:** {hospital_info.get("formatted_address", "Address not available")}
📞 **Phone:** {hospital_info.get("formatted_phone_number", "Phone not available")}
⭐ **Rating:** {hospital_info.get("rating", "No rating")}
🌐 **Website:** {hospital_info.get("website", "Website not available")}
🕒 **Status:** {"Open now" if hospital_info.get("opening_hours", {}).get("open_now") else "Status unknown"}
"""
                    hospitals.append(hospital_text)
        
        if not hospitals:
            return f"📍 **Location Detected:** {location_str}\n\n❌ No hospitals found in your area. You may need to expand your search radius."
        
        # Create formatted response
        response_text = f"""🌍 **Your Location:** {location_str}
🔍 **Search Radius:** {radius/1000} km
🏥 **Found {len(hospitals)} hospitals near you:**

{chr(10).join(hospitals)}

🚨 **EMERGENCY:** For medical emergencies, call **108** immediately (India Emergency Number)

💡 **Note:** This information is for reference only. For emergencies, always call 108 first before going to any hospital."""

        return response_text
        
    except Exception as e:
        return f"❌ Error finding hospitals: {str(e)}"

# Create FunctionTool wrapper for proper ADK compatibility
find_hospitals_tool = FunctionTool(func=find_nearby_hospitals)

# Create the Hospital Finder Agent with auto-location detection
hospital_finder_agent = Agent(
    name="hospital_finder",
    model="gemini-2.0-flash",
    description=(
        "Medical facility locator that automatically detects user location and finds nearby hospitals using Google Places API. "
        "Provides hospital information including addresses, phone numbers, ratings, and hours for India."
    ),
    instruction=HOSPITAL_FINDER_PROMPT,
    tools=[find_hospitals_tool],
) 