from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configuration of the flask application
app.config.from_object('config')

# Database manipulation using SQLAlchemy
db = SQLAlchemy(app)

# Routes
from routes import setup_routes
setup_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
