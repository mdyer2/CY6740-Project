from application import app, db
from model import User, Message

with app.app_context():
    # Create tables
    db.create_all()

    # Create a new user
    user = User(username='john_doe', email='john@example.com')
    user.set_password('mypassword')
    db.session.add(user)
    db.session.commit()

    # Verify password
    print(user.check_password('mypassword'))  # Should print True

    # Create a new message
    message = Message(sender_id=user.id, receiver_id=2, content='Hello, World!')
    db.session.add(message)
    db.session.commit()

    # Print message
    print(message)
