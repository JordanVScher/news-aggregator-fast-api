from sys import exit
import os
from dotenv import load_dotenv

load_dotenv()

PYTHON_ENV = os.getenv("PYTHON_ENV") or "DEV"
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

if not NEWS_API_KEY:
    exit("Fatal Error: NEWS_API_KEY must be supplied")
