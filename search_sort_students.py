from student_registration import get_int


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


def student_data_tools(students):
    while True:
        print("\n=== Search, Sort, and Manage Student Data ===")
        print("1. Sorting and Searching of Student IDs")
        print("2. Event Participation Analysis")
        print("3. Back to main menu")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            sorting_and_searching(students)
        elif choice == "2":
            event_participation_analysis()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Try again.")
