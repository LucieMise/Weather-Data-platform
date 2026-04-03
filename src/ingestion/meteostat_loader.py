from datetime import datetime
from pathlib import Path

import pandas as pd
import meteostat as ms
from meteostat import Point


def load_historical_weather_data(
    latitude: float,
    longitude: float,
    start: datetime,
    end: datetime,
    city_name: str = "unknown_city",
    save_to_csv: bool = False,
    output_dir: str = "data/raw",
):
    print(f"Loading data for {city_name}...")
    print(f"Coordinates: ({latitude}, {longitude})")
    print(f"Date range: {start.date()} to {end.date()}")

    location = Point(latitude, longitude)

    try:
        stations_df = ms.stations.nearby(location,limit=1)

        print("Nearby stations:")
        print(stations_df)

        if stations_df.empty:
            print("No nearby station found.")
            return None

        station_id = stations_df.index[0]
        print(f"Using station id: {station_id}")

        data = ms.daily(station_id, start, end)
        df = data.fetch()
        

    except Exception as e:
        print("Error while fetching Meteostat data:", e)
        return None

    if df is None or df.empty:
        print("No weather data returned.")
        return None

    df = df.reset_index()
    df = df.rename(columns={"time": "date"})
    df["city"] = city_name
    df["latitude"] = latitude
    df["longitude"] = longitude
    df["source"] = "meteostat"

    if save_to_csv:
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        file_path = output_path / f"{city_name.lower().replace(' ', '_')}_historical_weather.csv"
        df.to_csv(file_path, index=False)
        print(f"Saved to {file_path}")

    return df