"""
Filename: 02_Functions_Advanced.py
Purpose: Master advanced topics in Python functions including lambda,
nested functions, closures, and higher-order functions.
"""

# 🔹 Lambda Functions (Anonymous Functions)
"""
Lambda functions are small anonymous functions defined using the lambda keyword.
Syntax: lambda arguments: expression
"""

square = lambda x: x * x
print("Square:", square(5))  # Output: 25

add = lambda a, b: a + b
print("Sum:", add(3, 4))  # Output: 7

# Practical Use Example
nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, nums))
print("Squared List:", squared)


# 🔹 Nested Functions
"""
Function defined inside another function. Useful for encapsulating logic.
"""

def outer():
    print("Outer Function")

    def inner():
        print("Inner Function")

    inner()

outer()


# 🔹 Closures
"""
Closures remember values from their enclosing lexical scope even if the outer function has finished.
"""

def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

triple = make_multiplier(3)
print("Triple of 5:", triple(5))  # Output: 15


# 🔹 Higher Order Functions (HOF)
"""
Functions that accept other functions as arguments or return them.
"""

def apply_operation(operation, a, b):
    return operation(a, b)

print("Using add:", apply_operation(lambda x, y: x + y, 4, 6))
print("Using power:", apply_operation(pow, 2, 3))


# 🔹 Built-in HOFs: map(), filter(), reduce()

# map(): Apply a function to all items
squares = list(map(lambda x: x**2, [1, 2, 3, 4]))
print("Squares:", squares)

# filter(): Filter items based on a condition
even_nums = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))
print("Even Numbers:", even_nums)

# reduce(): Cumulative operation from functools
from functools import reduce
sum_total = reduce(lambda x, y: x + y, [1, 2, 3, 4])
print("Sum using reduce:", sum_total)


# 🔹 Practice Tasks
"""
1. Write a lambda that returns cube of a number
2. Create a closure that generates a multiplier (like double, triple)
3. Use map/filter/reduce to analyze a list of numbers
"""


# ✅ End of File 02_Functions_Advanced.py
"""
Add this as your second file for Python Mastery.
Next file will cover modules: 03_Modules_BuiltCustom.py
"""
