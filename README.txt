WEATHER DASHBOARD PROJECT
PROJECT OVERVIEW
A full-stack weather application built with Flask that provides real-time weather information, forecasts, and search history storage. The application fetches data from WeatherAPI and displays it through an interactive web interface with database persistence.

FEATURES
Real-time Weather Data: Current conditions, temperature, humidity, wind speed

Hourly Forecasts: 24-hour detailed weather predictions

Astronomical Data: Sunrise, sunset, moon phase information

Search History: Automatic storage of all weather queries in SQLite database

Multiple Endpoints: RESTful API for frontend integration and simple HTML views

Error Handling: Comprehensive error management for API failures and user inputs

TECHNICAL STACK
Backend Framework: Flask (Python)

External API: WeatherAPI.com

Database: SQLite3

HTTP Requests: Python Requests library

Frontend: HTML templates with JavaScript for dynamic content

Data Format: JSON for API responses

PROJECT STRUCTURE
weather_dashboard/
│
├── app.py (Main Flask application)
├── weather.db (SQLite database, auto-generated)
├── templates/ (HTML templates directory)
│ ├── index.html (Landing page)
│ └── app.html (Main application interface)
└── README.txt (This documentation file)

INSTALLATION & SETUP
Prerequisites
Python 3.8 or higher

pip (Python package manager)

Internet connection for API calls

Step-by-Step Installation
Create project directory
mkdir weather_dashboard
cd weather_dashboard

Create virtual environment (recommended)
python -m venv venv

On Windows: venv\Scripts\activate
On Mac/Linux: source venv/bin/activate

Install required packages
pip install flask requests

Get WeatherAPI key

Visit weatherapi.com

Sign up for a free account

Get your API key from the dashboard

Configure API key

Open app.py in a text editor

Replace the api_key variable with your actual key (line 24 in app.py):
api_key = "YOUR_API_KEY_HERE"

Run the application
python app.py

Access the dashboard

Open your web browser

Navigate to: http://localhost:5000

APPLICATION ROUTES
Main Endpoints
/ - Landing Page

Default route showing index.html

Introduction to the weather dashboard

/app - Main Application

Full-featured weather dashboard interface

Requires city parameter: /app?city=Berlin

/api/weather - JSON API Endpoint

Returns weather data in JSON format

Usage: /api/weather?city=London

Includes current weather, hourly forecast, and astronomical data

/simple - Simplified Version

Lightweight endpoint for testing

Usage: /simple?city=Paris

DATABASE OPERATIONS
Schema
The application creates and uses a SQLite database (weather.db) with the following structure:

CREATE TABLE IF NOT EXISTS weather_data (
city TEXT,
weather TEXT,
temp REAL,
feels REAL,
humidity INTEGER,
wind_speed REAL,
uv_index REAL
)

Database Access
To view stored data:
sqlite3 weather.db

Then run SQL commands:
-- Enable formatting
.mode column
.headers on

-- View all data
SELECT * FROM weather_data;

-- View recent entries
SELECT * FROM weather_data ORDER BY rowid DESC LIMIT 10;

-- Count total searches
SELECT COUNT(*) as total_searches FROM weather_data;

HOW IT WORKS
1. User Input Flow
User enters city -> Flask receives request -> Calls WeatherAPI -> Processes JSON ->
Saves to database -> Returns data to frontend -> Updates interface

2. API Integration
Two API calls: current weather and 1-day forecast

Error handling for invalid cities or API issues

Rate limiting consideration (1000 calls/month on free tier)

3. Data Processing
JSON responses parsed for key weather metrics

Data formatted for both API responses and HTML rendering

Automatic timestamp recording for each search

CODE STRUCTURE
Main Functions
save() function (lines 5-18)

Handles database operations

Creates table if not exists

Inserts weather data with error handling

get_weather_data() function (lines 26-42)

Makes API calls to WeatherAPI

Fetches both current and forecast data

Includes exception handling for API errors

Route Handlers (lines 44-116)

Four main routes with specific purposes

Consistent error handling across all endpoints

Database saving integrated into data flow

ERROR HANDLING
The application includes comprehensive error handling for:

Invalid city names or locations

WeatherAPI service unavailability

Database connection issues

Missing or incorrect API parameters

Network connectivity problems

CUSTOMIZATION OPTIONS
Extending the Application
Add More Weather Metrics

Modify the save() function to store additional data

Update API response processing to include new fields

Enhance Frontend Display

Modify app.html template for better visualization

Add charts or graphs using JavaScript libraries

Additional Features

User authentication for personalized history

Email or SMS weather alerts

Historical data analysis and trends

TROUBLESHOOTING
Common Issues
Application won't start

Check Python and Flask installation

Verify no other service is using port 5000

API errors

Confirm WeatherAPI key is valid and active

Check internet connectivity

Verify rate limit hasn't been exceeded

Database issues

Ensure write permissions in project directory

Check SQLite3 is available in Python environment

Template errors

Verify templates directory exists with required files

Check HTML files for syntax errors

SECURITY NOTES
API key is embedded in code (for development only)

In production, use environment variables for sensitive data

Consider input validation and sanitization for production use

Implement rate limiting for public-facing deployments

PERFORMANCE CONSIDERATIONS
SQLite database suitable for light to medium usage

API calls cached temporarily to reduce external requests

Consider database indexing for large search histories

Implement connection pooling for high-traffic scenarios

DEPLOYMENT OPTIONS
Local Deployment
Use built-in Flask server for development

Accessible only on local machine

Production Deployment
Use WSGI server (Gunicorn, uWSGI)

Reverse proxy with Nginx or Apache

Environment variables for configuration

Proper logging and monitoring setup

MAINTENANCE
Regular Tasks
Monitor API usage and rate limits

Backup weather database periodically

Update dependencies for security patches

Review and rotate API keys as needed

Scaling Considerations
Migrate from SQLite to PostgreSQL for larger datasets

Implement caching layer for frequent city queries

Consider load balancing for high availability

SUPPORT AND CONTACT
For questions or issues with the Weather Dashboard:

Review this documentation thoroughly

Check Flask and WeatherAPI documentation

Consult Python and web development resources

LICENSE AND ATTRIBUTION
Flask Framework: BSD License

WeatherAPI: Terms of weatherapi.com

Application Code: Provided for educational purposes

