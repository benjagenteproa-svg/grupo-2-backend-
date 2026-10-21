from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_PATH = os.getenv("DATABASE_PATH", "database.db")
APP_TITLE     = os.getenv("APP_TITLE", "API")
APP_VERSION   = os.getenv("APP_VERSION", "1.0.0")