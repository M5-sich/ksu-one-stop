from Data.CourseData import courses
from Data.UserData import users

class BursarActions:
    def view_all_student_tuition(self):
        print("\n Tuition Summary for All Students:")
        for username, info in users.items():
            if info["role"] == "student":
                enrolled = info.get("enrolled_courses", [])
                total = sum(courses[c]["cost"] for c in enrolled if c in courses)
                print(f"- {username}: ${total}")

    def view_individual_tuition(self):
        student = input("Enter student username: ")
        if student not in users or users[student]["role"] != "student":
            print("Invalid student.")
            return

        enrolled = users[student].get("enrolled_courses", [])
        total = sum(courses[c]["cost"] for c in enrolled if c in courses)

        print(f"\nTuition Summary for {student}:")
        for c in enrolled:
            if c in courses:
                print(f"  {c}: ${courses[c]['cost']}")
        print(f"\nTotal: ${total}")