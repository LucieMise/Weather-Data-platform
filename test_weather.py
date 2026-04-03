from src.ingestion.weather_client import get_weather 
from src.ingestion.multiple_city_weather_client import multiple_city_weather

result = get_weather("Nairobi")
print(result)


results = multiple_city_weather("London, New York")
print(results)