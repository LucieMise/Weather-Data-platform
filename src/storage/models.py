'''
This module defines the ORM model for storing weather data in the database. 
It uses SQLAlchemy to define a Weather class that maps to a weather_history table in the database. 
Each instance of Weather represents a record of weather information for a specific city, including temperature, humidity, description, and timestamp.
'''
from sqlalchemy import Column, Integer, String, Float,DateTime
from datetime import datetime
from .db import Base

class CurrentWeather(Base):
    __tablename__ = "current_weather"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String, nullable=False, index=True)
    temperature = Column(Float, nullable=False)
    humidity = Column(Integer, nullable=False)
    pressure = Column(Integer, nullable=True)
    description = Column(String, nullable=True)
    timestamp_utc = Column(String, nullable=False)
    source = Column(String, default="openweather")

class HistoricalWeather(Base):
    __tablename__ = "historical_weather"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String, nullable=False, index=True)
    date = Column(String, nullable=False, index=True)
    tavg = Column(Float, nullable=True)
    tmin = Column(Float, nullable=True)
    tmax = Column(Float, nullable=True)
    prcp = Column(Float, nullable=True)
    wspd = Column(Float, nullable=True)
    pres = Column(Float, nullable=True)
    source = Column(String, default="meteostat")