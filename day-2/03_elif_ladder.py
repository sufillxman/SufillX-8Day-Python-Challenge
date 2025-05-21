# Notes: elif Ladder in Python
# 1. What is an elif Ladder?
# The elif ladder is a way to check multiple conditions in sequence.
# It stands for "else if".
# It is used after an initial if statement and before an optional final else.
# Only the first condition that evaluates to True will execute its block; the rest are skipped.
# 2. How Does It Work?
# Python checks each condition from top to bottom.
# As soon as it finds a True condition, it runs that block and skips the rest.
# If none of the conditions are True, the else block (if present) runs.

'''
if condition1:
       Block 1
elif condition2:
       Block 2
elif condition3:
       Block 3
else:
   Block 4

'''

# How it works:
# The program checks the first if condition.
# If it's True, that block runs and the rest are skipped.
# If it's False, it checks the next elif condition.
# This continues down the ladder.
# If none of the conditions are True, the else block runs (if present).



# Example

'''
number = 15

if number < 10:
    print("Number is less than 10")
elif number < 20:
    print("Number is between 10 and 19")
elif number < 30:
    print("Number is between 20 and 29")
else:
    print("Number is 30 or more")

'''

# Output:
# Number is between 10 and 19

# Key Points
# Only the first True condition's block runs.
# You can have as many elif as needed.
# else is optional and runs if none of the above are True.


# Real-Life Example
# Scenario: Suppose you want to decide what to wear based on the weather.

'''
weather = "rainy"

if weather == "sunny":
    print("Wear sunglasses.")
elif weather == "rainy":
    print("Take an umbrella.")
elif weather == "snowy":
    print("Wear a coat.")
else:
    print("Check the weather forecast.")
'''

# Output:
# Take an umbrella

# Improved Example: Grading System
# Let's make a better example: Assigning grades based on marks.

'''
marks = 85

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")
'''

# Output:
# Grade: A


# Key Points
# Use elif when you have more than two conditions.
# Only one block will execute, even if multiple conditions are True.
# Helps keep code clean and readable.
# Tip:
# Always order your conditions from most specific to least specific to avoid logic errors.
