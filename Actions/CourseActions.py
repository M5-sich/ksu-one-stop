from Data.CourseData import courses
from Data.UserData import users

class CourseActions:
    def __init__(self, username):
        self.username = username

    def view_courses(self):
        print("\nAvailable Courses:\n")
        for code, info in courses.items():
            print(f"{code}")
            print(f"  Description: {info['description']}")
            print(f"  Professor: {info['professor']}")
            print(f"  Credit Hours: {info['credit_hours']}")
            print(f"  Seats Available: {info['seats_available']}")
            print()

    def enroll(self, course_code):
        student = users[self.username]
        enrolled = student.setdefault("enrolled_courses", [])

        if course_code not in courses:
            print("Course not found.")
            return

        if courses[course_code]["seats_available"] <= 0:
            print("No seats available for this course.")
            return

        if course_code in enrolled:
            print("Already enrolled in this course.")
            return

        enrolled.append(course_code)
        courses[course_code]["seats_available"] -= 1
        print(f"Enrolled in {course_code} successfully!")

    def drop(self, course_code):
        student = users[self.username]
        enrolled = student.get("enrolled_courses", [])

        if course_code not in enrolled:
            print("You're not enrolled in this course.")
            return

        enrolled.remove(course_code)
        courses[course_code]["seats_available"] += 1
        print(f"Dropped {course_code} successfully.")

    def view_enrolled_courses(self):
        student = users[self.username]
        enrolled = student.get("enrolled_courses", [])

        if not enrolled:
            print("You're not enrolled in any courses.")
            return

        print("\nYour Enrolled Courses:\n")
        for code in enrolled:
            info = courses[code]
            print(f"{code}")
            print(f"  Description: {info['description']}")
            print(f"  Professor: {info['professor']}")
            print(f"  Credit Hours: {info['credit_hours']}")
            print(f"  Seats Available: {info['seats_available']}")
            print()