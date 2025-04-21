from Validation import Login
from Actions.CourseActions import CourseActions
from Data.UserData import users
from Actions.AdvisorActions import AdvisorActions
from Actions.RegistrarActions import RegistrarActions
from Actions.AdminActions import AdminActions
from Actions.DeveloperActions import DeveloperActions
from Actions.BursarActions import BursarActions

shouldContinueMain = True
shouldContinue = True
mainAttempts = 0
attempts = 0

# ----------------------------------------------------------------------------------------------------------------------#
# Menu Methods
def student_main_menu(username):
    student_actions = CourseActions(username)

    while True:
        print("\nWhat would you like to do?\n"
              "1) View Available Courses\n"
              "2) Enroll in a Course\n"
              "3) View Enrolled Courses\n"
              "4) Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            student_actions.view_courses()
        elif choice == "2":
            course_code = input("Enter the course code to enroll: ").upper()
            student_actions.enroll(course_code)
        elif choice == "3":
            student_actions.view_enrolled_courses()
        elif choice == "4":
            print("Logging out...\n")
            break
        else:
            print("Invalid input. Please try again.")


def advisor_main_menu():
    advisor = AdvisorActions()
    while True:
        print("\nAdvisor Menu:\n"
              "1) View Student Course History\n"
              "2) Schedule Advising Session\n"
              "3) Recommend Courses for Graduation\n"
              "4) Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            advisor.view_student_history()
        elif choice == "2":
            advisor.schedule_advising_session()
        elif choice == "3":
            advisor.recommend_courses()
        elif choice == "4":
            print("Logging out...\n")
            break
        else:
            print("Invalid input. Please try again.")


def registrar_main_menu():
    registrar = RegistrarActions()
    while True:
        print("\nRegistrar Menu:\n"
              "1) View All Student Enrollments\n"
              "2) Enroll a Student in a Course\n"
              "3) Drop a Student from a Course\n"
              "4) Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            registrar.view_all_enrollments()
        elif choice == "2":
            registrar.enroll_student_in_course()
        elif choice == "3":
            registrar.drop_student_from_course()
        elif choice == "4":
            print("Logging out...\n")
            break
        else:
            print("Invalid input. Please try again.")


def admin_main_menu():
    admin = AdminActions()
    while True:
        print("\nAdmin Menu:\n"
              "1) View All Users\n"
              "2) Add New User\n"
              "3) Delete User\n"
              "4) Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            admin.view_all_users()
        elif choice == "2":
            admin.add_user()
        elif choice == "3":
            admin.delete_user()
        elif choice == "4":
            print("Logging out...\n")
            break
        else:
            print("Invalid input. Please try again.")


def developer_main_menu():
    developer = DeveloperActions()
    while True:
        print("\nDeveloper Menu:\n"
              "1) View All Raw Course Data\n"
              "2) View All Raw User Data\n"
              "3) Reset All Course Seat Counts\n"
              "4) Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            developer.view_all_course_data()
        elif choice == "2":
            developer.view_all_user_data()
        elif choice == "3":
            developer.reset_all_course_seats()
        elif choice == "4":
            print("Logging out...\n")
            break
        else:
            print("Invalid input. Please try again.")


def bursar_main_menu():
    bursar = BursarActions()
    while True:
        print("\nBursar Menu:\n"
              "1) View All Student Tuition\n"
              "2) View Individual Student Tuition\n"
              "3) Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            bursar.view_all_student_tuition()
        elif choice == "2":
            bursar.view_individual_tuition()
        elif choice == "3":
            print("Logging out...\n")
            break
        else:
            print("Invalid input. Please try again.")

# ----------------------------------------------------------------------------------------------------------------------#
# Login Flow

print("[Welcome to the KSU one-stop!]")

shouldContinueMain = True
mainAttempts = 0

while shouldContinueMain:
    print("Designation list choices: \n"
          "    1) Student\n"
          "    2) Advisor\n"
          "    3) Registrar\n"
          "    4) Admin\n"
          "    5) Developer\n"
          "    6) Bursar\n"
          "    7) Exit Program")
    usertype = int(input("Designation: "))

    if usertype == 7:
        print("Program Exited")
        shouldContinueMain = False

    elif usertype < 1 or usertype > 7:
        print("Invalid designation.")

    else:
        shouldContinue = True
        attempts = 0

        while shouldContinue:
            if attempts < 3:
                username = input("Username: ")
                password = input("Password: ")

                login = Login(username, password)

                if login.validate():
                    print("Login successful!")

                    if usertype == 1:
                        print("Student menu loading...")
                        student_main_menu(username)
                    elif usertype == 2:
                        print("Advisor menu loading...")
                        advisor_main_menu()
                    elif usertype == 3:
                        print("Registrar menu loading...")
                        registrar_main_menu()
                    elif usertype == 4:
                        print("Admin menu loading...")
                        admin_main_menu()
                    elif usertype == 5:
                        print("Developer menu loading...")
                        developer_main_menu()
                    elif usertype == 6:
                        print("Bursar menu loading...")
                        bursar_main_menu()

                    shouldContinue = False
                else:
                    attempts += 1
                    print("Incorrect Username or Password.")
                    print(f"You have {3 - attempts} attempts left.")
            else:
                print("Too many attempts. Please wait 1 hour until next attempt.")
                shouldContinue = False
                shouldContinueMain = False