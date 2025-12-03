1. Features:
-Flask web interface and API endpoints
-Real-time weather data using WeatherAPI
-1-day forecast including hourly data
-Automatic saving of weather results into SQLite (weather.db)

Multiple pages:
  /app → main weather application UI
  /simple → simplified weather page
  /api/weather → JSON API response

2. Installation & Setup:
Install these if you don't already have them:
  
  pip install flask requests

Install sqlite3 if you want to see the database too (optional)

After this open the python file, then run the code. Look at your terminal and there will be this link http://127.0.0.1:5000/ (this is a local host you wont get hacked). Press control + left mouse button. And this is it you are welcome.

3. Database (SQLite)
The application automatically creates *weather.db* and the table below:

TABLE: weather_data

Columns:
-city
-weather
-temp
-feels
-humidity
-wind_speed
-uv_index

To inspect the database:

    sqlite3 weather.db
    SELECT * FROM weather_data;

For a better view:

    .mode column
    .headers on

4. API

It's no problem if you don't have an API key, because we included one ourselves for free

The response includes:
-current weather data
-astronomical data
-hourly forecast

5. File Structure
Source/         application code
Templates/      HTML files (index.html, app.html)
weather.db      SQLite database
README.txt      this file

6. Notes
-Replace the API key with your own from WeatherAPI.com, if you want... (it's free!)
-The database will keep growing with each request unless cleaned manually (average user won't care anyways)

7. Open Source
As the title says, use it for whatever you like.


