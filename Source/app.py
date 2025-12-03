from flask import Flask, render_template, request, jsonify
import requests
import sqlite3

def save(city, weather, temp, feels, hum, wind, uv):
    try:
        conn = sqlite3.connect("weather.db")
        conn.execute("""CREATE TABLE IF NOT EXISTS weather_data 
                       (city, weather, temp, feels, humidity, wind_speed, uv_index)""")
        conn.execute("INSERT INTO weather_data VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (city, weather, temp, feels, hum, wind, uv))
        conn.commit()
        conn.close()
        print(f"Saved weather data for {city} to database")
    except Exception as e:
        print(f"Error saving to database: {e}")

app = Flask(__name__)
api_key = "e34a8c84ce634c08929170718250607"
def get_weather_data(city):
    """Shared function to get weather data for any endpoint"""
    try:
        # Get current weather
        current_url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
        current_res = requests.get(current_url)
        current_res.raise_for_status()
        current = current_res.json()
        
        # Get forecast (1 day)
        forecast_url = f"https://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=1"
        forecast_res = requests.get(forecast_url)
        forecast_res.raise_for_status()
        forecast = forecast_res.json()
        
        return current, forecast
    except Exception as e:
        raise Exception(f"Weather API error: {e}")

@app.route("/")
def landing_page():
    return render_template("index.html")

@app.route("/app")
def app_page():
    return render_template("app.html")

@app.route("/api/weather")
def api_weather():
    """JSON API endpoint"""
    city = request.args.get("city", "Berlin")  # Default to Berlin
    
    try:
        current, forecast = get_weather_data(city)
        
        # Save to database
        save(
            city,
            current["current"]["condition"]["text"],
            current["current"]["temp_c"],
            current["current"]["feelslike_c"],
            current["current"]["humidity"],
            current["current"]["wind_kph"],
            current["current"]["uv"]
        )
        
        response = {
            "city": city,
            "current": current["current"],
            "astro": forecast["forecast"]["forecastday"][0]["astro"],
            "hourly": forecast["forecast"]["forecastday"][0]["hour"]
        }
        
        return jsonify(response)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/simple")
def simple_weather_page():
    """HTML page endpoint - uses the same data as API"""
    city = request.args.get("city", "Berlin")
    
    try:
        current, forecast = get_weather_data(city)
        
        # Save to database
        save(
            city,
            current["current"]["condition"]["text"],
            current["current"]["temp_c"],
            current["current"]["feelslike_c"],
            current["current"]["humidity"],
            current["current"]["wind_kph"],
            current["current"]["uv"]
        )
        
        weather_data = {
            "city": city,
            "temp": current["current"]["temp_c"],
            "feels_like": current["current"]["feelslike_c"],
            "humidity": current["current"]["humidity"],
            "wind_speed": current["current"]["wind_kph"],
            "uv_index": current["current"]["uv"],
            "condition": current["current"]["condition"]["text"],
            "hourly_forecast": forecast["forecast"]["forecastday"][0]["hour"]
        }
        
        return render_template("app.html", **weather_data)
        
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)
