import csv


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
