# Student Grade Tracker

def get_letter_grade(score):  
    """get_letter_grade(score) function returns letter grade when numeric score is provided"""

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
    """print_summary(student_list) function prints a summary of student data collected """

    print("\nStudent Summary:")
    for student in student_list: # for-loop 

        print(f"{student['name']}: {student['class']} {student['score']}")


def save_to_file(student_list):
    """save_to_file(student_list) sales all of student data to 'grades.txt', one student per line"""

    with open("grades.txt", "w") as file: 
        for student in student_list:
            file.write(f"{student['name']}: {student['class']} {student['grade']}\n")


def main():
    """main() function collects student data, summarizes it, and saves it to a file."""

    print("Welcome to the Student Grade Tracker!\n")

    students = []

    while True:                 # main input loop
        raw_name = input("Enter student name: ")
        name = raw_name.strip().title()

        class_name = input("Enter class:").strip().title()

        while True:             # data validation loop                                         
            score_input = input("Enter score (0-100):").strip() 

            try:
                score = float(score_input)
                if 0 <= score <= 100:
                    break
                else:
                    print("Error: Score must be between 0 and 100")
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

        add_more = input("\nWould you like to add another student? (y/n): ").strip().lower()
        if add_more != 'y':
            break
    
    print_summary(students)                           
    save_to_file(students)                              
    print("\nStudent data saved to grades.txt")            

with open("grades.txt", "w") as file:

    main()