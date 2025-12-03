WEATHER DASHBOARD PROJECT
PROJECT OVERVIEW
Full-stack Flask application providing real-time weather data.
Fetches information from WeatherAPI and displays through interactive web interface.
Stores search history in local SQLite database for future reference.

FEATURES
-Real-time Weather Data: Current conditions, temperature, humidity, wind speed.
-Hourly Forecasts: 24-hour detailed weather predictions.
-Astronomical Data: Sunrise, sunset.
-Search History: Automatic storage of all weather queries in SQLite database.
-Multiple Endpoints: RESTful API for frontend integration and simple HTML views.
-Error Handling: Comprehensive error management for API failures and user inputs.

TECHNICAL STACK
Backend Framework: Flask (Python)
External API: WeatherAPI.com
Database: SQLite3
HTTP Requests: Python Requests library
Frontend: HTML templates with JavaScript for dynamic content

PROJECT STRUCTURE
weather_dashboard/
├── app.py (Main Flask application)
├── weather.db (SQLite database, auto-generated)
├── templates/ (HTML templates directory)
│ ├── index.html (Landing page)
│ └── app.html (Main application interface)
└── README.txt (This documentation file)

INSTALLATION & SETUP
Prerequisites: Python 3.8+, pip, internet connection.
Create directory: mkdir weather_dashboard && cd weather_dashboard
Install packages: pip install flask requests
Get API key from weatherapi.com (free account)

APPLICATION ROUTES
/ → Landing page (index.html)
/app → Main dashboard (use ?city=Berlin)
/api/weather → JSON API endpoint (use ?city=London)

DATABASE OPERATIONS
Schema: CREATE TABLE weather_data (city, weather, temp, feels, humidity, wind_speed, uv_index)
View data: sqlite3 weather.db then run queries.
Sample queries:
.mode column
.headers on
SELECT * FROM weather_data;
SELECT COUNT(*) FROM weather_data;

HOW IT WORKS
User enters city → Flask receives request → Calls WeatherAPI → Processes JSON → Saves to database → Returns data to frontend → Updates interface.

CODE STRUCTURE
save() function: Handles database insertion.
get_weather_data(): Makes API calls to WeatherAPI.
Route handlers: Four main routes with error handling.

ERROR HANDLING
Manages invalid city names, API unavailability, database issues, missing parameters, network problems.

CUSTOMIZATION
Add more weather metrics by modifying save() and API processing.
Enhance frontend by editing app.html template.
Add features like user authentication, alerts, or historical analysis.

TROUBLESHOOTING
App won't start: Check Python/Flask installation, port 5000 availability.
API errors: Confirm API key, internet, rate limit.
Database issues: Check write permissions, SQLite installation.
Template errors: Verify templates directory and HTML files.

DEPLOYMENT
Development: Built-in Flask server.
Production: Use WSGI server (Gunicorn) with reverse proxy (Nginx).

LICENSE
Flask: BSD License. WeatherAPI: Terms of weatherapi.com. Code: Educational use.


