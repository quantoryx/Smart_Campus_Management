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
