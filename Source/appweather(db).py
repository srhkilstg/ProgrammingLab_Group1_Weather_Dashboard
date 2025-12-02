from flask import Flask, render_template, request, jsonify
import requests
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import json
import os
import sqlite3  

def save(city, weather, temp, feels, hum, wind, uv):
        conn = sqlite3.connect("weather.db")
        conn.execute("CREATE TABLE IF NOT EXISTS weather_data (city, weather, temp, feels, humidity, wind_speed, uv_index)")
        conn.execute("INSERT INTO weather_data VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (city, weather, temp, feels, hum, wind, uv))
        conn.commit()
        conn.close()

app = Flask(__name__)

api_key = "e34a8c84ce634c08929170718250607"

@app.route("/")
def landing_page():
    return render_template("index.html")

@app.route("/app")
def app_page():
    return render_template("app.html")   

@app.route("/api/weather")
def api_weather():
    city = request.args.get("city")
    if not city:
        return jsonify({"error": "city is required"}), 400

    try:
        # Current weather
        url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
        current_res = requests.get(url)
        current_res.raise_for_status()
        current = current_res.json()

        # Forecast (for hourly + sunrise/sunset)
        forecast_url = (
            f"https://api.weatherapi.com/v1/forecast.json?"
            f"key={api_key}&q={city}&days=1&aqi=yes&alerts=yes"
        )
        forecast_res = requests.get(forecast_url)
        forecast_res.raise_for_status()
        forecast = forecast_res.json()

        response = {
            "city": city,
            "current": current["current"],
            "astro": forecast["forecast"]["forecastday"][0]["astro"],
            "hourly": forecast["forecast"]["forecastday"][0]["hour"]
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/simple", methods=["GET"])
def simple_weather_page():
    city = request.args.get("city")

    if not city:
        city = "Berlin"

    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        weather = data["current"]["condition"]["text"]
        temp = data["current"]["temp_c"]
        feels_like = data["current"]["feelslike_c"]
        humidity = data["current"]["humidity"]
        wind_speed = data["current"]["wind_kph"]
        uv_index = data["current"]["uv"]

        save(city, weather, temp, feels_like, humidity, wind_speed, uv_index)

    except Exception as e:
        return f"Error: {e}"

    weather_json = {
        "Temp_C": temp,
        "FeelsLike_C": feels_like,
        "Humidity": humidity,
        "Wind_kph": wind_speed,
        "UV_Index": uv_index
    }

    with open("static/weather.json", "w") as f:
        json.dump(weather_json, f, indent=4)

    # Bar chart
    labels = ["Temp (C)", "Feels Like", "Humidity", "Wind", "UV"]
    values = [temp, feels_like, humidity, wind_speed, uv_index]

    plt.figure(figsize=(6, 4))
    plt.bar(labels, values)
    plt.title(f"Weather data for {city}")
    plt.tight_layout()
    plt.savefig("static/chart.png")
    plt.close()

    # Forecast chart
    forecast_url = f"https://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=1"
    try:
        response = requests.get(forecast_url)
        forecast_data = response.json()

        hours = forecast_data["forecast"]["forecastday"][0]["hour"]
        times = [h["time"].split(" ")[1] for h in hours]
        temps = [h["temp_c"] for h in hours]

        if times:
            plt.figure(figsize=(10, 5))
            plt.plot(times, temps, marker="o")
            plt.title("Today's Temperature Curve")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.savefig("static/forecast.png")
            plt.close()

    except:
        pass

    return render_template("app.html", city=city)


if __name__ == "__main__":
    app.run(debug=True)
