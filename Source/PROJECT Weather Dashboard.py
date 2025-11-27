import requests
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

print("Welcome back! Please enter the city's first letter in capital.")

api_key = "e34a8c84ce634c08929170718250607"

city = input("Enter your city: ")

url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    weather = data["current"]["condition"]["text"]
    temp = data["current"]["temp_c"]
    Feels_Like = data["current"]["feelslike_c"]
    Humidity = data["current"]["humidity"]
    WindSpeed = data["current"]["wind_kph"]
    UvIndex = data["current"]["uv"]
except Exception as e:
    print("Error:", e)
else:
    print(
        f"Weather in {city}: {weather}, {temp}°C",
        f"Feels Like: {Feels_Like}°C",
        f"Humidity: {Humidity}%",
        f"Wind Speed: {WindSpeed} kph",
        f"UvIndex: {UvIndex}"
    )

    # Visualization part
    labels = ["Temp (C)", "Feels Like (C)", "Humidity (%)", "Wind (kph)", "UV Index"]
    values = [temp, Feels_Like, Humidity, WindSpeed, UvIndex]

    plt.figure(figsize=(6,4))
    plt.bar(labels, values)
    plt.title(f"Weather data for {city}")
    plt.ylabel("Value")
    plt.ylim(-10, 80)
    plt.tight_layout()
    plt.show()
 
