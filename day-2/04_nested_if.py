# Certainly! Let's understand nested if statements in Python with a clear explanation and a real-life example.

# What is a Nested If Statement?
# A nested if is an if statement inside another if statement. It allows you to check multiple conditions in a hierarchical way—only checking the inner condition if the outer one is true.

# Syntax Example
'''
if condition1:
    # code block
    if condition2:
        # code block
'''

# eal-Life Example
# Scenario:
# Suppose you want to check if a person is eligible to vote and, if yes, whether they are eligible for a senior citizen discount.

# To vote: Age must be 18 or above.
# For senior citizen discount: Age must be 60 or above.
# Python Code Example


'''
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
    if age >= 60:
        print("You are also eligible for the senior citizen discount.")
    else:
        print("You are not eligible for the senior citizen discount.")
else:
    print("You are not eligible to vote.")
'''


# How it Works
# The outer if checks if the person is 18 or older.
# If true, it prints voting eligibility and checks the inner if for age 60 or above.
# If the outer if is false, it skips the inner check.
# Real-Life Analogy
# Think of entering a club:

# First gate: Are you 18+? (Outer if)
# Second gate inside: Are you 60+? (Inner if for special lounge)
# Gotcha
# The inner if only runs if the outer if is true.
# Indentation is important in Python to define which code belongs to which block.

# Here are 3 different examples using nested if statements in Python, each with a real-life scenario:

'''
# Example 1: Checking exam pass and grade
marks = int(input("Enter your marks: "))
if marks >= 33:
    print("You passed the exam.")
    if marks >= 75:
        print("You got distinction!")
    else:
        print("You did not get distinction.")
else:
    print("You failed the exam.")
    
'''
'''
# Example 2: ATM withdrawal eligibility
balance = 5000
withdraw = int(input("Enter amount to withdraw: "))
if withdraw <= balance:
    print("Withdrawal possible.")
    if withdraw > 2000:
        print("Large withdrawal, please confirm with OTP.")
    else:
        print("Withdrawal processed.")
else:
    print("Insufficient balance.")

'''

'''
# Example 3: Movie ticket pricing based on age and day
age = int(input("Enter your age: "))
day = input("Enter day (weekday/weekend): ")
if age < 12:
    print("Child ticket.")
    if day == "weekend":
        print("Discounted child ticket for weekend!")
    else:
        print("Regular child ticket.")
else:
    print("Adult ticket.")

'''