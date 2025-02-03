import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

def get_current_weather():
    print(f"*** Getting the weather ... ***\n")
    city ="addis ababa"
    # city = input(f"Please enter a city name: ")
    request_url  = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY_WEATHER")}&q={city}&units=metric'
    weather_data =requests.get(request_url).json()
    pprint(weather_data)
    print(f'\nCurrent weather for {weather_data["name"]}:')
    print(f'\nThe temp is {weather_data["main"]["temp"]:.1f}°')
    print(f'\n{weather_data["weather"][0]["description"].capitalize()} and feels like {weather_data["main"]["feels_like"]:.1f}°\n')
get_current_weather()