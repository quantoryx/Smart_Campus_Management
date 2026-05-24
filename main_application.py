from course_enrollment import course_enrollment
from directory_scanner import directory_scanning_module
from fee_calculation import fee_calculation
from file_manager import file_handling_module
from performance_analytics import performance_analytics
from search_sort_students import student_data_tools
from student_records import display_student_records
from student_registration import register_student


def main():
    students = []

    while True:
        print("\n=== Smart Campus Information System ===")
        print("1. Student Registration and Grade Evaluation")
        print("2. Course Enrollment Management")
        print("3. Student Records Management")
        print("4. Search, Sort, and Manage Student Data")
        print("5. Student Fee Calculation")
        print("6. File Handling for Academic Records")
        print("7. Directory Scanning")
        print("8. Student Performance Analytics")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            register_student(students)
        elif choice == "2":
            course_enrollment(students)
        elif choice == "3":
            display_student_records(students)
        elif choice == "4":
            student_data_tools(students)
        elif choice == "5":
            fee_calculation(students)
        elif choice == "6":
            file_handling_module(students)
        elif choice == "7":
            directory_scanning_module()
        elif choice == "8":
            performance_analytics(students)
        elif choice == "0":
            print("Exiting Smart Campus Information System.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
