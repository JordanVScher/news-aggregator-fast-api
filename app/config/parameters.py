from sys import exit
import os
from dotenv import load_dotenv

load_dotenv()

PYTHON_ENV = os.getenv("PYTHON_ENV") or "DEV"
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")
