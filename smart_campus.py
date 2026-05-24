import csv
import os


class MissingFileOrFolderError(Exception):
    """Raised when a folder is empty during directory scanning."""


def evaluate_grade(score):
    if 90 <= score <= 100:
        return "A", "Excellent"
    if 75 <= score < 90:
        return "B", "Very Good"
    if 60 <= score < 75:
        return "C", "Good"
    if 40 <= score < 60:
        return "D", "Average"
    return "F", "Needs Improvement"


def get_int(prompt, allow_blank=False, default=None):
    while True:
        value = input(prompt).strip()
        if allow_blank and value == "":
            return default
        try:
            return int(value)
        except ValueError:
            print("Please enter a valid integer.")


def get_float(prompt, allow_blank=False, default=None):
    while True:
        value = input(prompt).strip()
        if allow_blank and value == "":
            return default
        try:
            return float(value)
        except ValueError:
            print("Please enter a valid number.")


def generate_student_id(students):
    if not students:
        return 101
    return max(student["id"] for student in students) + 1


def find_student(students, student_id):
    for student in students:
        if student["id"] == student_id:
            return student
    return None


def register_student(students):
    print("\n=== Student Registration and Grade Evaluation ===")
    name = input("Enter student name: ").strip()
    if not name:
        print("Student name cannot be empty.")
        return

    age = get_int("Enter student age: ")
    exam_score = get_float("Enter exam score (0-100): ")
    if exam_score < 0 or exam_score > 100:
        print("Score must be between 0 and 100.")
        return

    grade, remark = evaluate_grade(exam_score)
    student_id = generate_student_id(students)

    subject_scores = {}
    add_subjects = input(
        "Do you want to add Math, Science, and English scores? (y/n): "
    ).strip().lower()
    if add_subjects == "y":
        math_score = get_float("Enter Math score: ")
        science_score = get_float("Enter Science score: ")
        english_score = get_float("Enter English score: ")
        subject_scores = {
            "Math": math_score,
            "Science": science_score,
            "English": english_score,
        }
        grades = [math_score, science_score, english_score]
    else:
        grades = [exam_score]

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "score": exam_score,
        "grade": grade,
        "remark": remark,
        "grades": grades,
        "subject_scores": subject_scores,
        "courses": [],
        "fees": {
            "tuition_fee": 0.0,
            "hostel_fee": 0.0,
            "transportation_fee": 0.0,
            "total_fee": 0.0,
        },
    }
    students.append(student)

    print("\n--- Student Report ---")
    print("Student ID:", student["id"])
    print("Name:", student["name"])
    print("Score:", student["score"])
    print("Grade:", student["grade"])
    print("Performance Remark:", student["remark"])


def course_enrollment(students):
    print("\n=== Course Enrollment Management System ===")
    if not students:
        print("No students registered yet.")
        return

    student_id = get_int("Enter student ID: ")
    student = find_student(students, student_id)
    if not student:
        print("Student not found.")
        return

    max_courses = 5
    while True:
        if len(student["courses"]) >= max_courses:
            print("Maximum course limit reached.")
            break

        course_name = input("Enter course name (or 'done' to finish): ").strip()
        if course_name.lower() == "done":
            break
        if not course_name:
            print("Course name cannot be empty. Skipping entry...")
            continue

        credits = input("Enter credit value: ").strip()
        if not credits.isdigit():
            print("Invalid credit value. Skipping entry...")
            continue

        credits = int(credits)
        if credits <= 0:
            print("Credit must be positive. Skipping entry...")
            continue

        student["courses"].append((course_name, credits))
        print(f"Course '{course_name}' with {credits} credits added.")

    print("\n--- Enrollment Report ---")
    for course, credit in student["courses"]:
        print(f"Course: {course}, Credits: {credit}")
    print("Total courses enrolled:", len(student["courses"]))


def display_student_records(students):
    print("\n=== Student Records ===")
    if not students:
        print("No student records available.")
        return

    for student in students:
        print(f"ID: {student['id']}")
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Grades: {student['grades']}")
        print(f"Exam Score: {student['score']}")
        print(f"Grade: {student['grade']}")
        print(f"Remark: {student['remark']}")
        print(f"Courses: {student['courses']}")
        print("-" * 30)


def event_participation_analysis():
    print("\n=== Event Participation Analysis ===")
    event_a_input = input("Enter Event A participants separated by commas: ").strip()
    event_b_input = input("Enter Event B participants separated by commas: ").strip()

    event_a = {name.strip() for name in event_a_input.split(",") if name.strip()}
    event_b = {name.strip() for name in event_b_input.split(",") if name.strip()}

    if not event_a and not event_b:
        print("No event participant data entered.")
        return

    common_participants = event_a & event_b
    all_participants = event_a | event_b
    only_event_a = event_a - event_b

    print("Common Participants:", common_participants)
    print("All Participants:", all_participants)
    print("Only Event A Participants:", only_event_a)


def bubble_sort(values):
    sorted_values = values[:]
    n = len(sorted_values)
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_values[j] > sorted_values[j + 1]:
                sorted_values[j], sorted_values[j + 1] = (
                    sorted_values[j + 1],
                    sorted_values[j],
                )
    return sorted_values


def selection_sort(values):
    sorted_values = values[:]
    n = len(sorted_values)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if sorted_values[j] < sorted_values[min_index]:
                min_index = j
        sorted_values[i], sorted_values[min_index] = (
            sorted_values[min_index],
            sorted_values[i],
        )
    return sorted_values


def linear_search(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1


def binary_search(values, target):
    low = 0
    high = len(values) - 1
    while low <= high:
        mid = (low + high) // 2
        if values[mid] == target:
            return mid
        if values[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def sorting_and_searching(students):
    print("\n=== Sorting and Searching of Student IDs ===")
    if not students:
        print("No students registered yet.")
        return

    student_ids = [student["id"] for student in students]
    print("Original IDs:", student_ids)

    bubble_sorted_ids = bubble_sort(student_ids)
    selection_sorted_ids = selection_sort(student_ids)

    print("Sorted IDs (Bubble Sort):", bubble_sorted_ids)
    print("Sorted IDs (Selection Sort):", selection_sorted_ids)

    target = get_int("Enter student ID to search: ")

    linear_index = linear_search(bubble_sorted_ids, target)
    if linear_index != -1:
        print("Linear Search: ID", target, "found at index", linear_index)
    else:
        print("Linear Search: ID not found")

    binary_index = binary_search(bubble_sorted_ids, target)
    if binary_index != -1:
        print("Binary Search: ID", target, "found at index", binary_index)
    else:
        print("Binary Search: ID not found")


def calculate_fee(tuition_fee, hostel_fee=0.0, transportation_fee=0.0):
    return tuition_fee + hostel_fee + transportation_fee


def fee_calculation(students):
    print("\n=== Student Fee Calculation ===")
    if not students:
        print("No students registered yet.")
        return

    student_id = get_int("Enter student ID: ")
    student = find_student(students, student_id)
    if not student:
        print("Student not found.")
        return

    tuition_fee = get_float("Enter tuition fee: ")
    hostel_fee = get_float("Enter hostel fee (press Enter for 0): ", True, 0.0)
    transportation_fee = get_float(
        "Enter transportation fee (press Enter for 0): ", True, 0.0
    )

    total_fee = calculate_fee(tuition_fee, hostel_fee, transportation_fee)
    student["fees"] = {
        "tuition_fee": tuition_fee,
        "hostel_fee": hostel_fee,
        "transportation_fee": transportation_fee,
        "total_fee": total_fee,
    }

    print(f"Total fee for {student['name']}: {total_fee}")


def write_records_to_file(students, filename="student_records.csv"):
    if not students:
        print("No students registered yet.")
        return

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Age", "Marks", "Grade", "Remark", "TotalFee"])
        for student in students:
            writer.writerow(
                [
                    student["id"],
                    student["name"],
                    student["age"],
                    student["score"],
                    student["grade"],
                    student["remark"],
                    student["fees"]["total_fee"],
                ]
            )

    print(f"Student records written to {filename} successfully.")


def read_records_from_file(filename="student_records.csv"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            print("\nReading stored records:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"{filename} not found.")


def generate_file_report(filename="student_records.csv"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            rows = list(reader)

        if not rows:
            print("No records available in the file.")
            return

        total_students = len(rows)
        total_marks = sum(float(row["Marks"]) for row in rows)
        top_student = max(rows, key=lambda row: float(row["Marks"]))
        average_marks = total_marks / total_students

        print("\nGenerating Report:")
        print("Total Students:", total_students)
        print("Average Marks:", round(average_marks, 2))
        print(
            "Top Student:",
            top_student["Name"],
            "with",
            top_student["Marks"],
            "marks",
        )
    except FileNotFoundError:
        print(f"{filename} not found.")


def file_handling_module(students):
    print("\n=== File Handling for Student Academic Records ===")
    filename = input(
        "Enter file name to use (press Enter for student_records.csv): "
    ).strip()
    if not filename:
        filename = "student_records.csv"

    while True:
        print("\n1. Write student details to file")
        print("2. Read stored records from file")
        print("3. Generate file report")
        print("4. Back to main menu")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            write_records_to_file(students, filename)
        elif choice == "2":
            read_records_from_file(filename)
        elif choice == "3":
            generate_file_report(filename)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")


def scan_directory(path):
    try:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Invalid directory path: {path}")

        print(f"\nScanning directory: {path}\n")
        for root, dirs, files in os.walk(path):
            level = root.replace(path, "").count(os.sep)
            indent = " " * 4 * level
            print(f"{indent}{os.path.basename(root)}/")
            sub_indent = " " * 4 * (level + 1)
            for file_name in files:
                print(f"{sub_indent}{file_name}")

            if not files and not dirs:
                raise MissingFileOrFolderError(f"Empty folder detected: {root}")
    except FileNotFoundError as error:
        print("Error:", error)
    except MissingFileOrFolderError as error:
        print("Custom Error:", error)
    except Exception as error:
        print("Unexpected Error:", error)


def directory_scanning_module():
    print("\n=== Directory Scanning with Exception Handling ===")
    directory_path = input("Enter the directory path to scan: ").strip()
    scan_directory(directory_path)


def build_performance_dataframe_from_students(students, pd):
    data = []
    for student in students:
        subject_scores = student["subject_scores"]
        if {"Math", "Science", "English"} <= subject_scores.keys():
            data.append(
                {
                    "Name": student["name"],
                    "Math": subject_scores["Math"],
                    "Science": subject_scores["Science"],
                    "English": subject_scores["English"],
                }
            )
    if not data:
        return None
    return pd.DataFrame(data)


def performance_analytics(students):
    print("\n=== Student Performance Analysis ===")
    try:
        import numpy as np
        import pandas as pd
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("Required libraries are not installed: NumPy, Pandas, or Matplotlib.")
        return

    print("1. Analyze data from CSV file")
    print("2. Analyze registered students with subject scores")
    choice = input("Enter your choice: ").strip()

    try:
        if choice == "1":
            csv_path = input(
                "Enter CSV file path (press Enter for student_performance.csv): "
            ).strip()
            if not csv_path:
                csv_path = "student_performance.csv"
            df = pd.read_csv(csv_path)
        elif choice == "2":
            df = build_performance_dataframe_from_students(students, pd)
            if df is None or df.empty:
                print("No registered students have complete subject scores.")
                return
            csv_path = "student_performance_from_students.csv"
            df.to_csv(csv_path, index=False)
            print(f"Performance data saved to {csv_path}")
        else:
            print("Invalid choice.")
            return

        required_columns = {"Name", "Math", "Science", "English"}
        if not required_columns.issubset(df.columns):
            print("CSV file must contain Name, Math, Science, and English columns.")
            return

        print("\n--- Raw Data ---")
        print(df.head())

        print("\n--- Statistical Summary ---")
        print(df.describe())

        scores = df[["Math", "Science", "English"]].to_numpy(dtype=float)
        mean_scores = np.mean(scores, axis=0)
        median_scores = np.median(scores, axis=0)
        std_dev_scores = np.std(scores, axis=0)

        print("\n--- NumPy Analysis ---")
        print("Mean Scores (Math, Science, English):", mean_scores)
        print("Median Scores (Math, Science, English):", median_scores)
        print("Standard Deviation (Math, Science, English):", std_dev_scores)

        top_math = df.loc[df["Math"].idxmax(), "Name"]
        top_science = df.loc[df["Science"].idxmax(), "Name"]
        top_english = df.loc[df["English"].idxmax(), "Name"]

        print("\n--- Top Performers ---")
        print("Math:", top_math)
        print("Science:", top_science)
        print("English:", top_english)

        subjects = ["Math", "Science", "English"]
        plt.figure(figsize=(8, 5))
        plt.bar(subjects, mean_scores, color=["blue", "green", "orange"])
        plt.title("Average Scores per Subject")
        plt.xlabel("Subjects")
        plt.ylabel("Average Score")
        plt.tight_layout()
        plt.savefig("average_scores.png")
        plt.close()

        ax = df.plot(x="Name", y=["Math", "Science", "English"], kind="bar", figsize=(10, 6))
        ax.set_title("Student Performance Comparison")
        ax.set_ylabel("Scores")
        plt.tight_layout()
        plt.savefig("student_performance_comparison.png")
        plt.close()

        print("\nCharts saved as average_scores.png and student_performance_comparison.png")
    except FileNotFoundError:
        print("Error: The CSV file was not found. Please check the file path.")
    except Exception as error:
        print("Unexpected Error:", error)


def main():
    students = []

    while True:
        print("\n=== Smart Campus Information System ===")
        print("1. Student Registration and Grade Evaluation")
        print("2. Course Enrollment Management")
        print("3. Student Records Management")
        print("4. Event Participation Analysis")
        print("5. Sorting and Searching of Student IDs")
        print("6. Student Fee Calculation")
        print("7. File Handling for Academic Records")
        print("8. Directory Scanning")
        print("9. Student Performance Analytics")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            register_student(students)
        elif choice == "2":
            course_enrollment(students)
        elif choice == "3":
            display_student_records(students)
        elif choice == "4":
            event_participation_analysis()
        elif choice == "5":
            sorting_and_searching(students)
        elif choice == "6":
            fee_calculation(students)
        elif choice == "7":
            file_handling_module(students)
        elif choice == "8":
            directory_scanning_module()
        elif choice == "9":
            performance_analytics(students)
        elif choice == "0":
            print("Exiting Smart Campus Information System.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
