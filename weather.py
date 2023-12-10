import requests

def get_weather(city):
    api_key = "16f0c81559a532c62baaa67b13080b91"  
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(base_url)
    weather_data = response.json()

    if weather_data["cod"] == 200:
        weather_description = weather_data["weather"][0]["description"]
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        city_name = weather_data["name"]
        country = weather_data["sys"]["country"]

        print(f"Weather in {city_name}, {country}:")
        print(f"Description: {weather_description}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
    else:
        print("City not found. Please check the city name.")

if __name__ == "__main__":
    city_input = input("Enter the city name: ")
    get_weather(city_input)
