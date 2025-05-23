"""
Filename: 01_Functions_Basics.py
Purpose: Deep dive into basic function concepts in Python for mastery
"""

# 🔹 Introduction: Why Functions?
"""
Functions are reusable blocks of code designed to perform a single, related action.
They help break our program into smaller and modular chunks, making it more readable,
maintainable, and less error-prone.
"""

# 🔹 Function Syntax and Execution

def greet():
    print("Hello from the greet function!")

greet()  # Output: Hello from the greet function!


# 🔹 Parameters vs Arguments

def add(a, b):
    return a + b

print(add(10, 5))  # Parameters: a, b | Arguments: 10, 5


# 🔹 Return Statement

def square(n):
    return n * n

result = square(6)
print("Square:", result)


# 🔹 Default Arguments

def welcome(name="Guest"):
    print(f"Welcome, {name}!")

welcome()        # Output: Welcome, Guest!
welcome("Sufill")  # Output: Welcome, Sufill!


# 🔹 Positional vs Keyword Arguments

def student(name, age):
    print(f"{name} is {age} years old.")

student("Ali", 20)  # Positional
student(age=22, name="Ravi")  # Keyword


# 🔹 Variable-length Arguments

def total(*numbers):
    print("Total:", sum(numbers))

total(10, 20, 30, 40)


def profile(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

profile(name="Sufill", city="Rajkot", age=21)


# 🔹 Function Calling Function

def multiply(a, b):
    return a * b

def double_of_product(x, y):
    return multiply(x, y) * 2

print(double_of_product(3, 4))  # Output: 24


# 🔹 Practice Tasks (Recommended)
"""
1. Create a function that checks whether a number is even or odd
2. Create a function that returns both sum and average of a list of numbers
3. Build a small CLI that asks name, age and prints personalized message
"""


# ✅ End of File 01_Functions_Basics.py
"""
Save this file as the first part of your Python Mastery Repository.
It covers all foundational aspects of Python functions in detail.
Next: 02_Functions_Advanced.py will contain lambda, nested, closures and HOFs.
"""

