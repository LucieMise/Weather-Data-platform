from src.storage.db import SessionLocal
from src.storage.models import CurrentWeather, HistoricalWeather


def save_current_weather(data: dict):
    session = SessionLocal()
    try:
        weather = CurrentWeather(
            city=data["city"],
            temperature=data["temperature"],
            humidity=data["humidity"],
            pressure=data.get("pressure"),
            description=data.get("description"),
            timestamp_utc=str(data["timestamp_utc"]),
            source=data.get("source", "openweather"),
        )
        session.add(weather)
        session.commit()
        session.refresh(weather)
        return weather
    finally:
        session.close()


def save_historical_weather(df):
    session = SessionLocal()
    try:
        records = []

        for _, row in df.iterrows():
            record = HistoricalWeather(
                city=row["city"],
                date=str(row["date"]),
                tavg=row.get("tavg"),
                tmin=row.get("tmin"),
                tmax=row.get("tmax"),
                prcp=row.get("prcp"),
                wspd=row.get("wspd"),
                pres=row.get("pres"),
                source=row.get("source", "meteostat"),
            )
            records.append(record)

        session.add_all(records)
        session.commit()
        return len(records)
    finally:
        session.close()