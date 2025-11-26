import requests
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt 

print("Welcome back! Please enter the city's first letter in capital.")
def get_weather(city, api_key):
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
        return weather, temp, Feels_Like, Humidity, WindSpeed , UvIndex
    except (requests.RequestException, KeyError, IndexError) as e:
        print(f"Error: {e}")
        print(f"Response: {response.text if 'response' in locals() else 'No response'}")
        return None, None, None, None, None, None, None
def show_chart(city, temp, Feels_Like, Humidity, WindSpeed, UvIndex):
    labels = ["Temp (C)", "Feels Like (C)", "Humidity (%)", "Wind (kph)", "UV Index"]
    values = [temp, Feels_Like, Humidity, WindSpeed, UvIndex]

    plt.figure(figsize=(6,4))
    plt.bar(labels, values)
    plt.title(f"Weather data for {city}")
    plt.ylabel("Value")
    plt.ylim(-10, 80)
    plt.tight_layout()
    plt.show()

def main():
    api_key = "e34a8c84ce634c08929170718250607"

    city = input("Enter your city: ")
    weather, temp, Feels_Like, Humidity, WindSpeed, Uv= get_weather(city, api_key)

    if weather is None:
        print("Could not get weather data.")
        return

    print(f"Weather in {city}: {weather}, {temp}°C", 
          f"Feels Like: {Feels_Like}°C", 
          f"Humidity: {Humidity}%", 
          f"Wind Speed: {WindSpeed} kph", 
          f"UvIndex: {Uv}")  

    show_chart(city, temp, Feels_Like, Humidity, WindSpeed, Uv)
if __name__ == "__main__":
    main()
