from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import jwt
import os

# Import Config from configuration.py
from configuration import Config

app = Flask(__name__)
CORS(app)

# Configuration of the flask application
app.config.from_object(Config)

# Database manipulation using SQLAlchemy
db = SQLAlchemy(app)

# Import models
from model import User, Message

# Routes
@app.route('/')
def index():
    return jsonify({"message": "Hello, World!"})

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    email = data['email']
    password = data['password']
    if User.query.filter_by(email=email).first():
        return jsonify({'message': 'Email already registered'}), 400
    new_user = User(username=username, email=email)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']
    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        token = jwt.encode({'user_id': user.id, 'exp': datetime.utcnow() + datetime.timedelta(hours=1)}, app.config['SECRET_KEY'])
        return jsonify({'token': token})
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/send_message', methods=['POST'])
def send_message():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'message': 'Token is missing'}), 403
    try:
        data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
    except:
        return jsonify({'message': 'Token is invalid'}), 403
    user_id = data['user_id']
    data = request.get_json()
    receiver_id = data['receiver_id']
    content = data['content']
    new_message = Message(sender_id=user_id, receiver_id=receiver_id, content=content)
    db.session.add(new_message)
    db.session.commit()
    return jsonify({'message': 'Message sent successfully'}), 201

@app.route('/get_messages/<int:receiver_id>', methods=['GET'])
def get_messages(receiver_id):
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'message': 'Token is missing'}), 403
    try:
        data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
    except:
        return jsonify({'message': 'Token is invalid'}), 403
    user_id = data['user_id']
    messages = Message.query.filter((Message.sender_id == user_id) | (Message.receiver_id == user_id)).all()
    return jsonify([{'sender_id': msg.sender_id, 'receiver_id': msg.receiver_id, 'content': msg.content, 'timestamp': msg.timestamp} for msg in messages])

if __name__ == '__main__':
    app.run(debug=True)
