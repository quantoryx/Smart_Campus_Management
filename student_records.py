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
