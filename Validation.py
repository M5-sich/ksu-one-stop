from Data.UserData import users
from Data.CourseData import courses


class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def validate(self):
        if self.username in users:
            if self.password == users[self.username]["password"]:
                return True
            else:
                return False
        return False
