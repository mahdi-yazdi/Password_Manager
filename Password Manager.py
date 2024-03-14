class PasswordManager:
    def __init__(self):
        self.passwords = {}

    def add_password(self, website, password):
        self.passwords[website] = password

    def retrieve_password(self, website):
        return self.passwords.get(website, "Password not found")

    def update_password(self, website, new_password):
        if website in self.passwords:
            self.passwords[website] = new_password
            return True
        else:
            return False

# Example usage:
my_password_manager = PasswordManager()

# Add passwords
my_password_manager.add_password("example.com", "password123")
my_password_manager.add_password("google.com", "securepassword123")

# Retrieve passwords
print("Password for example.com:", my_password_manager.retrieve_password("example.com"))
print("Password for google.com:", my_password_manager.retrieve_password("google.com"))

# Update password
my_password_manager.update_password("example.com", "newpassword123")
print("Updated password for example.com:", my_password_manager.retrieve_password("example.com"))
