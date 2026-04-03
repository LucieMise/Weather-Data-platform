from src.storage.db import SessionLocal
from src.storage.models import HistoricalWeather


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