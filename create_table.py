from src.storage.db import engine, Base
from src.storage import models

Base.metadata.create_all(bind=engine)

print("Tables created successfully.")