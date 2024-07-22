import os

# Gets the directory path of the current file
basedir = '/home/ubuntu/CY6740-Project'

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'SecureChat'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'application.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
