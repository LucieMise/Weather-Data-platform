from datetime import datetime
from src.ingestion.meteostat_loader import load_historical_weather_data

df = load_historical_weather_data(
    latitude=-1.2921,
    longitude=36.8219,
    start=datetime(2022, 1, 1),
    end=datetime(2022, 12, 31),
    city_name="Nairobi",
    save_to_csv=True
)

if df is not None:
    print(df.head())
    print(df.columns)
    print(df.shape)
else:
    print("No weather data returned.")