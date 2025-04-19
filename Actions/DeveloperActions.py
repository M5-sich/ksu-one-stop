from Data.CourseData import courses
from Data.UserData import users

class DeveloperActions:
    def view_all_course_data(self):
        print("\n Raw Course Data:")
        for code, data in courses.items():
            print(f"\n{code}:")
            for key, value in data.items():
                print(f"  {key}: {value}")

    def view_all_user_data(self):
        print("\n Raw User Data:")
        for username, data in users.items():
            print(f"\n{username}:")
            for key, value in data.items():
                print(f"  {key}: {value}")

    def reset_all_course_seats(self):
        default_seat = 30
        for course in courses.values():
            course["seats"] = default_seat
        print(f"\n️ All course seats reset to {default_seat}.")