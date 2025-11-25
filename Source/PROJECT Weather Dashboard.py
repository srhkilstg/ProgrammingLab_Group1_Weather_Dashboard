import requests
from textblob import TextBlob

# Test print to confirm the script runs
print("Script is running...")

def get_weather(city, api_key):
    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        weather = data["current"]["condition"]["text"]  # e.g., "Partly cloudy"
        temp = data["current"]["temp_c"]  # temperature in Celsius
        return weather, temp
    except (requests.RequestException, KeyError, IndexError) as e:
        print(f"Error: {e}")
        print(f"Response: {response.text if 'response' in locals() else 'No response'}")
        return None, None


def main():
    api_key = "e34a8c84ce634c08929170718250607"  # Replace this with your own key if needed

    city = input("Enter your city: ")
    weather, temp = get_weather(city, api_key)

    if weather is None:
        print("Could not get weather data.")
        return

    print(f"Weather in {city}: {weather}, {temp}°C")

if __name__ == "__main__":
    main()