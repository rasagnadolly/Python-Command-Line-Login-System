import json
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def add_user(username, password, filename='users.json'):
    try:
        with open(filename, 'r') as f:
            users = json.load(f)
    except FileNotFoundError:
        users = {}

    users[username] = hash_password(password)

    with open(filename, 'w') as f:
        json.dump(users, f, indent=4)

    print(f"✅ User '{username}' added successfully.")

if __name__ == "__main__":
    u = input("New Username: ")
    p = input("New Password: ")
    add_user(u, p)

