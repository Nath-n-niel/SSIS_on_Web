import os
from dotenv import load_dotenv
from distutils.util import strtobool
import cloudinary
load_dotenv()

class Config:
        # Basic Flask configuration
    SECRET_KEY = os.getenv('SECRET_KEY')
    # SESSION_TYPE = 'filesystem'

    # Database configuration
    MYSQL_HOST = os.getenv('MYSQL_HOST')
    MYSQL_USER = os.getenv('MYSQL_USER')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
    MYSQL_DATABASE = os.getenv('MYSQL_DATABASE')

    SECRET_KEY = os.getenv('SECRET_KEY')
    WTF_CSRF_SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = os.getenv('FLASK_ENV') == 'development'