from Data.UserData import users
from Data.CourseData import courses


class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def validate(self):
        if self.username in users:
            if self.password == users[self.username]["password"]:
                return True  # Username and password match
            else:
                return False  # Username found, but password is wrong
        return False  # Username not found
