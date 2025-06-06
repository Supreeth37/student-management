# Contributor: Person 2 - User Management

class UserManager:
    def __init__(self):
        self.users = []
        self.user_id_counter = 1

    def register_user(self):
        name = input("Enter user name: ")
        email = input("Enter user email: ")

        user = {
            'id': self.user_id_counter,
            'name': name,
            'email': email
        }
        self.users.append(user)
        print(f"User '{name}' registered with ID {self.user_id_counter}.")
        self.user_id_counter += 1

    def view_users(self):
        if not self.users:
            print("No users registered.")
            return

        print("\nRegistered Users:")
        for user in self.users:
            print(f"ID: {user['id']} | Name: {user['name']} | Email: {user['email']}")

