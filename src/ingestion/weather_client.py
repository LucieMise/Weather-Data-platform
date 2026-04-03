'''
This module defines a WeatherClient class that interacts with the OpenWeatherMap API to fetch current weather data for a specified city.
It uses the requests library to make HTTP requests to the API and retrieves weather information such as temperature, humidity, and description.
The API key is loaded from an environment variable using the dotenv library for secure configuration management.
'''
import json
import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
DEFAULT_CACHE_TTL_SECONDS = 300
_ttl_env = os.getenv("WEATHER_CACHE_TTL_SECONDS")
try:
    CACHE_TTL_SECONDS = int(_ttl_env) if _ttl_env else DEFAULT_CACHE_TTL_SECONDS
except ValueError:
    CACHE_TTL_SECONDS = DEFAULT_CACHE_TTL_SECONDS

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

try:
    from src.cache.redis_client import redis_client
except Exception:
    redis_client = None

def _cache_key(city: str) -> str:
    normalized = city.strip().lower()
    return f"weather:{normalized}"


def write_to_cache(city: str, data: dict):
    if redis_client is not None:
        cache_key = _cache_key(city)
        try:
            redis_client.setex(cache_key, CACHE_TTL_SECONDS, json.dumps(data))
        except Exception:
            pass

def get_weather(city:str):
    city = city.strip()
    if not city:
        return {
            "error": "City name cannot be empty"
        }   
    cache_key = _cache_key(city)
    if redis_client is not None:
        try:
            cached = redis_client.get(cache_key)
        except Exception:
            cached = None
        if cached:
            try:
                return json.loads(cached)
            except Exception:
                pass

    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    if not API_KEY:
        return {
            "error": "API key is not configured"
        }
    
    response = requests.get(BASE_URL, params=params)
    data=response.json()

    if response.status_code != 200:
        return {
        "error": data.get("message", "Something went wrong")
     }
    result = {
        "city": data['name'],       
        "temperature": data['main']['temp'],
        "humidity": data['main']['humidity'],
        "pressure": data["main"]["pressure"],
        "description": data['weather'][0]['description'],
        "timestamp_utc": data["dt"],

    }
    write_to_cache(city, result)
    return result



