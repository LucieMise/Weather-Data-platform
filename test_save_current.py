from src.ingestion.weather_client import get_weather
from src.storage.repository import save_current_weather

weather_data = get_weather("Nairobi")
print("Fetched:", weather_data)

saved = save_current_weather(weather_data)
print("Saved record ID:", saved.id)


