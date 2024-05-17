from utils.user import User

class UserManager:
    def __init__(self):
        self.accounts = {}
        self.load_users()

    def load_users(self):
        try:
            with open('users.txt', 'r') as f:
                for line in f:
                    username, password = line.strip().split(',')
                    self.accounts[username] = User(username, password)
        except FileNotFoundError:
            print("User file not found.")
        except Exception as e:
            print(f"Error loading users: {e}")

    def save_users(self):
        with open('users.txt', 'w') as f:
            for username, user in self.accounts.items():
                f.write(f"{username},{user.password}\n")

    def validate_username(self, username):
        if len(username) < 4:
            print("Username must be at least 4 characters long.")
            return False
        elif username in self.accounts:
            print("Username already exists.")
            return False
        else:
            return True

    def validate_password(self, password):
        if len(password) < 8:
            print("Password must be at least 8 characters long.")
            return False
        else:
            return True

    def register_user(self):
        username = input("Enter username (at least 4 characters), or leave blank to cancel: ")
        if username == "":
            return
        elif self.validate_username(username):
            password = input("Enter password (at least 8 characters), or leave blank to cancel: ")
            if password == "":
                return
            elif self.validate_password(password):
                print("Registration Successful.")
                self.accounts[username] = User(username, password)
                self.save_users()

    def login_user(self):
        username = input("Enter username, or leave blank to cancel: ")
        if username in self.accounts:
            password = input("Enter password, or leave blank to cancel: ")
            if password == self.accounts[username].password:
                print(f"Welcome back, {username}!")
                return self.accounts[username]
            else:
                print("Incorrect password.")
                return None
        else:
            print("Username does not exist.")
            return None
