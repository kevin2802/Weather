import requests
import json

api_key = "4644c27759543eb889e6b103153efa28"
city = "New York"

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

response = requests.get(url)

if response.status_code == 200:
    data = json.loads(response.text)
    weather = data["weather"][0]["description"]
    temp = round(data["main"]["temp"] - 273.15, 1)
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    
    print(f"Current weather in {city}: {weather}")
    print(f"Temperature: {temp} °C")
    print(f"Humidity: {humidity}%")
    print(f"Wind speed: {wind_speed} m/s")
else:
    print(f"Error retrieving weather data: {response.status_code}")


