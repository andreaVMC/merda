from dotenv import load_dotenv
import os



class Config:
    load_dotenv()
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SECRET_KEY = 'a'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
