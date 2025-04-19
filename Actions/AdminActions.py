from Data.UserData import users

class AdminActions:
    def view_all_users(self):
        print("\n All Registered Users:")
        for username, data in users.items():
            print(f"- {username} ({data['role']})")

    def add_user(self):
        username = input("Enter new username: ")
        if username in users:
            print("Username already exists.")
            return

        password = input("Enter password for new user: ")
        role = input("Enter role (student, advisor, registrar, admin, developer, bursar): ").lower()

        if role not in ["student", "advisor", "registrar", "admin", "developer", "bursar"]:
            print("Invalid role.")
            return

        users[username] = {"password": password, "role": role}
        if role == "student":
            users[username]["enrolled_courses"] = []
            users[username]["history"] = []
            users[username]["recommended"] = []

        print(f" User '{username}' added successfully.")

    def delete_user(self):
        username = input("Enter username to delete: ")
        if username not in users:
            print("User not found.")
            return
        if users[username]["role"] == "admin":
            print("Cannot delete another admin.")
            return

        del users[username]
        print(f" User '{username}' has been deleted.")