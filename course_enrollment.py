from student_registration import find_student, get_int


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
