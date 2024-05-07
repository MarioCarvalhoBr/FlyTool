import os
from dotenv import load_dotenv

load_dotenv()

# Vars from .env
class GlobalConfig:
    SECRET_KEY =  os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER')

# Vars from .flaskenv
class FlaskConfig:
    FLASK_APP = os.getenv('FLASK_APP')
    FLASK_ENV = os.getenv('FLASK_ENV')
    FLASK_DEBUG = os.getenv('FLASK_DEBUG')
    