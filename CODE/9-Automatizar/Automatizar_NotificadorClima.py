# Notificador de clima em tempo real
import requests
import time

API_KEY = 'your_api_key'
CITY = 'New York'

def get_weather():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data['weather'][0]['description'], data['main']['temp'] - 273.15

while True:
    weather, temp = get_weather()
    print(f"Current weather in {CITY}: {weather}, {temp:.2f}°C")
    time.sleep(3600)  # Run every hour