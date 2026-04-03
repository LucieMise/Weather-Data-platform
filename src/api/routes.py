from fastapi import APIRouter, Query
from requests import session
from sqlalchemy.orm import Session 
from src.ingestion.multiple_city_weather_client import multiple_city_weather
from src.ingestion.weather_client import get_weather
from src.stoarge.database.db import SessionLocal
from src.stoarge.database.models import Weather

router = APIRouter()

@router.get("/")
def home():
    return {"message": "Welcome to the Weather API"}

@router.get("/current/{city}")
def weather(city: str):
    print(f"Fetching weather for {city}")
    session: Session = SessionLocal()
    weather_data = get_weather(city)
    session.close() 
    return weather_data

@router.get("/multiple")
def weather_multiple(
    cities: str = Query(..., description="Comma-separated list of cities")
):
    print("Received cities:", cities)

    session: Session = SessionLocal()
    try:
        weather_data = multiple_city_weather(cities)
        return weather_data
    finally:
        session.close()



