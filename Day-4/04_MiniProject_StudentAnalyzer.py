# 📘 04_MiniProject_StudentAnalyzer.py

"""
Filename: 04_MiniProject_StudentAnalyzer.py
Purpose: A complete mini project using functions, modules, and input validation
"""

# 🔹 Description
"""
This program collects student data, calculates average, grades, and displays a report.
"""

# 🔹 Module Import
import statistics

# 🔹 Functions

def calculate_average(marks):
    return statistics.mean(marks)

def get_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'

def display_report(name, marks):
    avg = calculate_average(marks)
    grade = get_grade(avg)
    print("\n--- Student Report ---")
    print("Name:", name)
    print("Marks:", marks)
    print("Average:", round(avg, 2))
    print("Grade:", grade)


# 🔹 Main Program

def main():
    name = input("Enter student name: ")
    marks = []
    for i in range(1, 6):
        while True:
            try:
                mark = float(input(f"Enter mark {i} (0-100): "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Please enter valid marks between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    display_report(name, marks)


if __name__ == '__main__':
    main()


# ✅ End of File 04_MiniProject_StudentAnalyzer.py
"""
This project puts everything together and gives a solid confidence boost.
You can further enhance it by:
- Adding file saving (CSV/JSON)
- Handling multiple students
- Generating summary statistics
"""
