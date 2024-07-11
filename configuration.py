import os

# Gets the directory path of the current file
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_very_secret_key'  # Secret key for sessions and security NEED TO ADD
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'application.db')  # Database URI for SQLite 
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable track modifications for better performance
