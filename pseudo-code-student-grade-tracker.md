# Pseudocode: Student Grade Tracker

## Program Overview

This program lets a user enter names and scores for multiple students, determines their letter grades, and saves the information to a file. It uses variables, lists, input/output, type conversion, loops, functions, conditionals, and file I/O.

## 1. Define a function to get the letter grade

- Name the function `get_letter_grade(score)`
- Input: a numeric score (0–100)
- Logic:
    - If the score is 90 or above, return 'A'
    - If the score is 80 or above (but less than 90), return 'B'
    - If the score is 70 or above (but less than 80), return 'C'
    - If the score is 60 or above (but less than 70), return 'D'
    - If the score is below 60, return 'F'
- Output: the corresponding letter grade (A, B, C, D, or F)



## 1. Define a function to print a summary of all students

- Name the function `print_summary(student_list)`
- Input: a list of student records, where each record includes the name, class, score, and letter grade
- Logic:
    - PRINT a heading "Student Summary:"
    - FOR each student in the list:
        - PRINT the student's name (properly formatted), score, and letter grade in the format:  
          `Name: score -> grade`



## 1. Define a function to save the data to a file

- Name the function `save_to_file(student_list)`
- Input: a list of student records
- Logic:
    - OPEN a file called "grades.txt" in write mode
    - FOR each student in the list:
        - Write the student's name, class, score, and grade to the file in the format:  
          `Name: score grade`
        - Each student should be written on a separate line
    - CLOSE the file after writing all data



## 1. Main Workflow

- PRINT a welcome message: "Welcome to the Student Grade Tracker!"
- CREATE an empty list called `students` to store each student's information
- Start a WHILE loop that will repeat for as long as the user wants to add students:
    1. ASK the user to enter a student name
        - FORMAT - Remove any extra spaces and capitalize each part of the name 
    1. ASK the user to enter a score for the student (0–100)
        - Remove extra spaces from the input
        - CONVERT the input to a numeric value (use float or int)
        - VALIDATE if the input is not a number or is outside the range 0–100, show an error and ask again
    1. CALL the `get_letter_grade(score)` function to get the student's letter grade
    1. Create a record (dictionary or tuple) containing the student's formatted name, score, and grade
    1. ADD the record to the `students` list
    1. ASK the user: "Add another student? (yes/no):"
        - If the answer is not "yes", exit the loop

- After the loop ends (no more students to add):
    1. CALL `print_summary(students)` to display all student information in a summary format
    1. CALL `save_to_file(students)` to save the student data to "grades.txt"
    1. PRINT a final message: "Student data saved to grades.txt"