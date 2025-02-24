# Sample user database (dictionary)
users = {"admin": "password123", "user1": "pass123"}

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users and users[username] == password:
        print("Login successful!")
    else:
        print("Invalid username or password.")

# Call the function to test login
login()
