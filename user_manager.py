import json
import os
from datetime import datetime

class UserManager:
    def __init__(self):
        self.users_file = "users.json"
        self.users = self.load_users()

    def load_users(self):
        """Load users from file"""
        if os.path.exists(self.users_file):
            try:
                with open(self.users_file, 'r') as f:
                    return json.load(f)
            except:
                return {}
        return {}

    def save_users(self):
        """Save users to file"""
        with open(self.users_file, 'w') as f:
            json.dump(self.users, f, indent=4)

    def add_user(self, username, password, email=""):
        """Add a new user"""
        if username in self.users:
            return False, "Username already exists"
        
        self.users[username] = {
            "password": password,
            "email": email,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "last_login": None
        }
        self.save_users()
        return True, "User created successfully"

    def verify_user(self, username, password):
        """Verify user credentials"""
        if username not in self.users:
            return False, "User not found"
        
        if self.users[username]["password"] != password:
            return False, "Invalid password"
        
        self.users[username]["last_login"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.save_users()
        return True, "Login successful"

    def get_user_info(self, username):
        """Get user information"""
        if username not in self.users:
            return None
        return self.users[username]

    def update_user(self, username, **kwargs):
        """Update user information"""
        if username not in self.users:
            return False, "User not found"
        
        for key, value in kwargs.items():
            if key in self.users[username]:
                self.users[username][key] = value
        
        self.save_users()
        return True, "User updated successfully"

    def delete_user(self, username):
        """Delete a user"""
        if username not in self.users:
            return False, "User not found"
        
        del self.users[username]
        self.save_users()
        return True, "User deleted successfully" 