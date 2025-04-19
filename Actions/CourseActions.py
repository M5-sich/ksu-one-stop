from Data.CourseData import courses


class CourseActions:
    def __init__(self):
        self.enrolled_courses = []

    def view_courses(self):
        print("\nAvailable Courses:\n")
        print(f"{'Course Code':<12} | {'Title':<25} | {'Instructor':<15} | {'Credits':<7} | {'Seats'}")
        print("-" * 75)

        for code, info in courses.items():
            print(
                f"{code:<12} | {info['title']:<25} | {info['instructor']:<15} | {info['credits']:<7} | {info['seats']}")
        print()

    def enroll(self, course_code):
        if course_code not in courses:
            print("Course not found.")
            return

        if courses[course_code]["seats"] <= 0:
            print("No seats available for this course.")
            return

        if course_code in self.enrolled_courses:
            print("Already enrolled in this course.")
            return

        self.enrolled_courses.append(course_code)
        courses[course_code]["seats"] -= 1
        print(f"Enrolled in {course_code} successfully!")

    def drop(self, course_code):
        if course_code not in self.enrolled_courses:
            print("You're not enrolled in this course.")
            return

        self.enrolled_courses.remove(course_code)
        courses[course_code]["seats"] += 1
        print(f"Dropped {course_code} successfully.")

    def view_my_courses(self):
        if not self.enrolled_courses:
            print("You're not enrolled in any courses.")
            return

        print("\nYour Enrolled Courses:")
        for code in self.enrolled_courses:
            info = courses[code]
            print(f"{code} - {info['title']} ({info['instructor']})")
