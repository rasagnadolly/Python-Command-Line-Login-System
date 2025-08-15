from auth import load_users, authenticate

def main():
    users = load_users()
    max_attempts = 3
    attempts = 0

    print("=== LOGIN SYSTEM ===")

    while attempts < max_attempts:
        username = input("Username: ")
        password = input("Password: ")

        if authenticate(username, password, users):
            print("✅ Login successful. Welcome,", username)
            return
        else:
            print("❌ Invalid username or password.")
            attempts += 1
            print(f"Attempts remaining: {max_attempts - attempts}")

    print("🚫 Too many failed attempts. Exiting...")

if __name__ == "__main__":
    main()