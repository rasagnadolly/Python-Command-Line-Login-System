import hashlib
import json

def hash_password(password):
    """Hash the password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def load_users(filename='users.json'):
    """Load users from the JSON file."""
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def authenticate(username, password, users):
    """Check if username and password match."""
    hashed = hash_password(password)
    return username in users and users[username] == hashed
