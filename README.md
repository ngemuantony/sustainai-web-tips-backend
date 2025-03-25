# SustainAI Tips Backend

A Flask-based backend service that generates personalized sustainability tips using the Google Gemini 1.5 Pro AI model. This service provides location-aware and habit-specific recommendations for sustainable living.

## Features

- 🤖 Powered by Google Gemini 1.5 Pro AI
- 📍 Location-aware recommendations
- 🎯 Personalized based on user habits
- 🏷️ Categorized tips output
- 🔄 CORS-enabled for frontend integration
- 🚀 Fast response times

## Tech Stack

- **Framework**: Flask
- **AI Model**: Google Gemini 1.5 Pro
- **Python Version**: 3.8+
- **Dependencies**: 
  - flask
  - flask-cors
  - google-generativeai
  - python-dotenv

## Getting Started

1. **Set Up Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. **Install Dependencies**

```bash
pip install -r requirements.txt
```

3. **Environment Setup**

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

4. **Run the Server**

```bash
python app.py
```

The server will start on `http://localhost:5000`

## Project Structure

```
backend/
├── app.py              # Main application file
├── requirements.txt    # Project dependencies
├── .env               # Environment variables
└── venv/              # Virtual environment
```

## API Endpoints

### Generate Sustainability Tips

```
POST /api/tips
```

**Request Body**:
```json
{
    "location": "string",  // e.g., "New York"
    "habits": "string"     // e.g., "driving car, using plastic bags"
}
```

**Response**:
```json
{
    "tips": [
        "## 1. Quick Wins",
        "* Tip 1...",
        "## 2. Sustainable Living",
        "* Tip 2...",
        // ... more categorized tips
    ]
}
```

## AI Prompt Structure

The Gemini AI model is prompted to generate tips in the following categories:
1. Quick Wins
2. Sustainable Living
3. Transportation & Mobility
4. Community & Social Impact
5. Environmental Protection

Each tip is:
- Location-specific
- Actionable and practical
- Cost-conscious
- Formatted in Markdown

## Error Handling

The backend implements error handling for:
- Invalid API requests
- AI model errors
- Missing environment variables
- CORS issues

## Security

- Environment variables for sensitive data
- CORS configuration for frontend access
- Input validation
- Error message sanitization

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## License

MIT License - feel free to use this project for learning and development!
