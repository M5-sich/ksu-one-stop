from Data.UserData import users
from Data.CourseData import courses

class RegistrarActions:
    def view_all_enrollments(self):
        print("\n All Student Enrollments:")
        for username, info in users.items():
            if info["role"] == "student":
                enrolled = info.get("enrolled_courses", [])
                print(f"\n{username}:")
                if enrolled:
                    for course in enrolled:
                        print(f"  - {course}")
                else:
                    print("  No courses enrolled.")

    def enroll_student_in_course(self):
        student = input("Enter student username: ")
        course = input("Enter course code: ").upper()

        if student not in users or users[student]["role"] != "student":
            print("Invalid student.")
            return
        if course not in courses:
            print("Invalid course code.")
            return
        if courses[course]["seats"] <= 0:
            print("No seats available.")
            return

        if course in users[student].get("enrolled_courses", []):
            print(f"{student} is already enrolled in {course}.")
            return

        users[student]["enrolled_courses"].append(course)
        courses[course]["seats"] -= 1
        print(f" {student} enrolled in {course} successfully.")

    def drop_student_from_course(self):
        student = input("Enter student username: ")
        course = input("Enter course code to drop: ").upper()

        if student not in users or users[student]["role"] != "student":
            print("Invalid student.")
            return
        if course not in users[student].get("enrolled_courses", []):
            print(f"{student} is not enrolled in {course}.")
            return

        users[student]["enrolled_courses"].remove(course)
        courses[course]["seats"] += 1
        print(f" {student} has been dropped from {course}.")