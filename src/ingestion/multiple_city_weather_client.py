
from src.ingestion.weather_client import get_weather


def multiple_city_weather(cities: str):
    city_list = [city.strip() for city in cities.split(",") if city.strip()]
    print("City list:", city_list)
    weather_data = []
    print("Calling get_weather for each city:")
    for city in city_list:
        print("Calling get_weather with:", city)
        city_weather = get_weather(city)
        print("Result:", city_weather)
        weather_data.append(city_weather)
    
    return {"weather_data": weather_data}