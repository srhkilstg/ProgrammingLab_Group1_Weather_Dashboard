from flask import Flask, render_template, request
import requests
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import json
import os

app = Flask(__name__)

api_key = "e34a8c84ce634c08929170718250607"

@app.route("/", methods=["GET"])
def home():
    city = request.args.get("city")

    # Current weather
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

    except Exception as e:
        return f"Error: {e}"

    # Save current weather JSON
    weather_json = {
        "Temp_C": temp,
        "FeelsLike_C": feels_like,
        "Humidity": humidity,
        "Wind_kph": wind_speed,
        "UV_Index": uv_index
    }

    with open("static/weather.json", "w") as f:
        json.dump(weather_json, f, indent=4)

    # Generate current weather chart
    labels = ["Temp (C)", "Feels Like (C)", "Humidity (%)", "Wind (kph)", "UV Index"]
    values = [temp, feels_like, humidity, wind_speed, uv_index]

    plt.figure(figsize=(6, 4))
    plt.bar(labels, values)
    plt.title(f"Weather data for {city}")
    plt.ylabel("Value")
    plt.ylim(-10, 80)
    plt.tight_layout()
    chart_path = os.path.join("static", "chart.png")
    plt.savefig(chart_path)
    plt.close()

    # Forecast weather
    forecast_url = f"https://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=1"
    try:
        response = requests.get(forecast_url)
        response.raise_for_status()
        forecast_data = response.json()

        hours = forecast_data["forecast"]["forecastday"][0]["hour"]
        times = [h["time"].split(" ")[1] for h in hours]
        temps = [h["temp_c"] for h in hours]
        humidity_values = [h["humidity"] for h in hours]

        if times:
            plt.figure(figsize=(12, 6))

            # Temperature plot
            plt.subplot(2, 1, 1)
            plt.plot(times, temps, marker='o')
            plt.title(f"Temperature Forecast for {city} Today")
            plt.xlabel("Time")
            plt.ylabel("Temperature (°C)")

            # Humidity plot
            plt.subplot(2, 1, 2)
            plt.plot(times, humidity_values, marker='s')
            plt.title(f"Humidity Forecast for {city} Today")
            plt.xlabel("Time")
            plt.ylabel("Humidity (%)")

            plt.tight_layout()
            forecast_path = os.path.join("static", "forecast.png")
            plt.savefig(forecast_path)
            plt.close()

    except Exception as e:
        print("Forecast error:", e)

    return render_template("app.html", city=city)


if __name__ == "__main__":
    app.run(debug=True)
