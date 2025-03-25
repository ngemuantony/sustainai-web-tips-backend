"""
SustainAI Tips Backend Server

This Flask application serves as the backend for the SustainAI Tips web application.
It uses the Google Gemini 1.5 Pro AI model to generate personalized sustainability tips
based on user location and habits.

Key Components:
    - Flask server with CORS support
    - Google Gemini AI integration
    - Structured prompt engineering
    - Error handling and validation
"""

import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Flask application
app = Flask(__name__)

# Configure CORS for frontend integration
CORS(app, resources={
    r"/api/*": {
        "origins": ["http://localhost:3000", "http://127.0.0.1:3000"],
        "methods": ["POST", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})

# Configure Google Gemini AI with API key
try:
    genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
except Exception as e:
    print("Error configuring Gemini AI:", str(e))

def generate_ai_tips(location: str, habits: str) -> list:
    """
    Generate personalized sustainability tips using Google Gemini AI.

    Args:
        location (str): User's location for location-specific tips
        habits (str): User's current habits to provide targeted recommendations

    Returns:
        list: List of markdown-formatted tips organized by categories

    Raises:
        Exception: If there's an error generating tips from the AI model
    """
    try:
        # Initialize Gemini 1.5 Pro model
        model = genai.GenerativeModel('gemini-1.5-pro')
        
        # Construct the prompt with specific instructions
        prompt = f"""
        Generate practical and personalized sustainability tips for someone in {location} with the following habits: {habits}.
        
        Format the response in markdown with the following categories:
        1. Quick Wins (Easy to implement immediately)
        2. Sustainable Living
        3. Transportation & Mobility
        4. Community & Social Impact
        5. Environmental Protection

        For each tip:
        - Make it specific to {location}
        - Include cost implications or savings
        - Make it actionable and practical
        - Consider local resources and infrastructure
        - Use bullet points with bold headers
        
        Start each category with a markdown header (##) and number.
        Format each tip as a markdown bullet point (*).
        Use bold (**) for tip headers.
        """

        # Generate response from AI model
        response = model.generate_content(prompt)
        
        # Split response into lines and clean up
        tips = response.text.strip().split('\n')
        return [tip.strip() for tip in tips if tip.strip()]

    except Exception as e:
        print("Error generating tips:", str(e))
        raise

@app.route('/api/tips', methods=['POST'])
def get_tips():
    """
    API endpoint to generate sustainability tips.
    
    Expects POST request with JSON body containing:
        - location: string
        - habits: string
    
    Returns:
        JSON response with generated tips or error message
    """
    try:
        # Extract data from request
        data = request.get_json()
        location = data.get('location', '').strip()
        habits = data.get('habits', '').strip()

        # Validate input
        if not location or not habits:
            return jsonify({
                'error': 'Please provide both location and habits'
            }), 400

        # Generate tips using AI
        tips = generate_ai_tips(location, habits)
        
        return jsonify({'tips': tips})

    except Exception as e:
        # Log error and return safe error message
        print("Error processing request:", str(e))
        return jsonify({
            'error': 'Failed to generate tips. Please try again.'
        }), 500

if __name__ == '__main__':
    # Run Flask development server
    app.run(debug=True)