import requests
import json
import tkinter as tk

api_key = "4644c27759543eb889e6b103153efa28"
city = "New York"

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

response = requests.get(url)

if response.status_code == 200:
    data = json.loads(response.text)
    weather = data["weather"][0]["description"]
    temp = round(data["main"]["temp"] - 273.15, 1)
    temp = temp *1.8
    temp +=32
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    if temp > 90:
        outfit = "T shirt + Shorts"
    elif temp > 70:
        outfit = "T shirt"
    elif temp> 55:
        outfit = "Hoodie"
    elif temp >45:
        outfit = "Jacket"
    elif temp <=45:
        outfit = "Parka/Long Coat"

    window = tk.Tk()
    window.title("Current")
    weather_label = tk.Label(window, text=f"Weather: {weather}")
    temp_label = tk.Label(window, text=f"Temperature: {temp} °F")
    humidity_label = tk.Label(window, text=f"Humidity: {humidity}%")
    wind_speed_label = tk.Label(window, text=f"Wind speed: {wind_speed} m/s") 
    outfit_label = tk.Label(window,text=f"Based off previous preferences you should wear: {outfit}")  

    weather_label.pack()
    temp_label.pack()
    humidity_label.pack()
    wind_speed_label.pack()
    outfit_label.pack()
    
    window.mainloop()

   # print(f"Current weather in {city}: {weather}")
   # print(f"Temperature: {temp} °F")
    # print(f"Humidity: {humidity}%")
   # print(f"Wind speed: {wind_speed} m/s")
    
else:
    print(f"Error retrieving weather data: {response.status_code}")


