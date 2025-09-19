users = {
    "admin": {"password": "admin123", "role": "admin"},
    "user": {"password": "user123", "role": "user"}
}

def login():
    username = input("Username: ")
    password = input("Password: ")
    user = users.get(username)
    if user and user["password"] == password:
        print(f"Welcome {username} ({user['role']})")
        return user
    return None
