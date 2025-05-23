"""
Filename: 03_Modules_BuiltCustom.py
Purpose: Understand built-in and custom modules, importing techniques, and practical examples
"""

# 🔹 What is a Module?
"""
A module is a Python file (.py) that contains definitions and code.
You can import it into other Python programs to reuse functions, variables, or classes.
"""

# 🔹 Built-in Modules Example
import math
import random

print("Square root of 49:", math.sqrt(49))
print("Random number between 1 and 10:", random.randint(1, 10))


# 🔹 Different Ways to Import

import math
print(math.pi)

from math import sqrt
print(sqrt(16))

from math import *
print(factorial(5))

import math as m
print(m.pow(2, 3))


# 🔹 Creating a Custom Module
# Step 1: Create a file named mymath.py with following code:
"""
# mymath.py

def add(a, b):
    return a + b

def cube(x):
    return x ** 3
"""

# Step 2: In main program
# import mymath
# print(mymath.add(4, 5))
# print(mymath.cube(3))


# 🔹 Checking All Functions in a Module
print(dir(math))  # Lists all attributes of math module


# 🔹 __name__ == '__main__'
"""
Used to prevent parts of code from running when the module is imported
"""

def greet():
    print("Hello from Module!")

if __name__ == '__main__':
    greet()  # This runs only when script is executed directly


# 🔹 Practice Tasks
"""
1. Create a custom module to handle basic math operations
2. Use random module to create a dice simulator
3. Import datetime and print current time in readable format
"""


# ✅ End of File 03_Modules_BuiltCustom.py
"""
Next: 04_MiniProject_StudentAnalyzer.py will use all these concepts together in a mini project.
"""
