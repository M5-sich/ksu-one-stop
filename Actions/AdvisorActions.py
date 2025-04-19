from Data.UserData import users

class AdvisorActions:
    def view_student_history(self):
        student_id = input("Enter student username (e.g., student1): ")
        if student_id in users and users[student_id]["role"] == "student":
            print(f"\nCourse History for {student_id}:")
            for course in users[student_id].get("history", []):
                print(f"- {course}")
        else:
            print("Student not found or invalid ID.")

    def schedule_advising_session(self):
        student_id = input("Enter student username (e.g., student1): ")
        session_date = input("Enter advising session date (e.g., 2024-04-25): ")
        print(f" Advising session scheduled with {student_id} on {session_date}.")

    def recommend_courses(self):
        student_id = input("Enter student username (e.g., student1): ")
        if student_id in users and users[student_id]["role"] == "student":
            print(f"\n📘 Recommended Courses for {student_id}:")
            for course in users[student_id].get("recommended", []):
                print(f"- {course}")
        else:
            print("Student not found or invalid ID.")