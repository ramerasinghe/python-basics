# Student Grade Tracker with Text-Based Menu

def get_letter_grade(score):
    """
    Returns the letter grade for a given numeric score.
    """
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def print_summary(student_list):
    """
    Prints a summary of all students, including their name, class, score, and letter grade.
    """
    if not student_list:
        print("\nNo student data to show.")
        return
    print("\nStudent Summary:")
    for student in student_list:
        print(f"{student['name']}: {student['class']} {student['score']} {student['grade']}")

def save_to_file(student_list):
    """
    Saves all student data to 'grades.txt', one student per line.
    """
    with open("grades.txt", "w") as file:
        for student in student_list:
            file.write(f"{student['name']}: {student['class']} {student['score']} {student['grade']}\n")

def add_student(students):
    """
    Adds a new student record to the students list.
    """
    raw_name = input("Enter student name: ")
    name = raw_name.strip().title()

    class_name = input("Enter class/subject name: ").strip().title()

    while True:
        score_input = input("Enter score (0–100): ").strip()
        try:
            score = float(score_input)
            if 0 <= score <= 100:
                break
            else:
                print("Error: Score must be between 0 and 100.")
        except ValueError:
            print("Error: Please enter a valid number.")

    grade = get_letter_grade(score)
    display_score = int(score) if score == int(score) else score
    students.append({
        'name': name,
        'class': class_name,
        'score': display_score,
        'grade': grade
    })
    print("Student added!")

def main_menu():
    """
    Displays the menu and handles user choices.
    """
    students = []
    print("Welcome to the Student Grade Tracker!\n")

    while True:
        print("\nPlease select an option:")
        print("1. Add a new student grade")
        print("2. View student summary")
        print("3. Save student data to file")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            print_summary(students)
        elif choice == "3":
            save_to_file(students)
            print("Student data saved to grades.txt")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main_menu()
