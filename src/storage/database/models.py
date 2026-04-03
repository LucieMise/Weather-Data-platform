'''
This module defines the ORM model for storing weather data in the database. 
It uses SQLAlchemy to define a Weather class that maps to a weather_history table in the database. 
Each instance of Weather represents a record of weather information for a specific city, including temperature, humidity, description, and timestamp.
'''
from sqlalchemy import Column, Integer, String, Float,DateTime
from datetime import datetime
from .db import Base

class Weather(Base):
    __tablename__ = 'weather_history'
    
    id = Column(Integer, primary_key=True, index=True)
    city = Column(String, index=True)
    temperature = Column(Float)
    humidity = Column(Float)
    description = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
