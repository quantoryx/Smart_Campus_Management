from student_registration import find_student, get_float, get_int


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
