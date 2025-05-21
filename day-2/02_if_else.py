# What is an if-else Statement?
# An if-else statement lets your program make decisions. It checks a condition (something that can be True or False).

# If the condition is True, it runs one block of code.
# If the condition is False, it runs another block of code.
# Real-Life Example
# Imagine:
# You want to go outside. If it’s raining, you take an umbrella. If it’s not raining, you don’t.

# How does this look in Python?

is_raining = True  # Change this to False to see the other result

if is_raining:
    print("Take an umbrella!")
else:
    print("No need for an umbrella.")


# Explanation:
# is_raining is a variable that can be True or False.
# if is_raining: checks if it’s raining.
# If it is raining, it prints: Take an umbrella!
# If it is not raining, it prints: No need for an umbrella.


# Notes for Beginners
# The if keyword starts the condition.
# The code under if runs only if the condition is True.
# The else keyword covers everything else (when the condition is False).
# Indentation (spaces before the code) is important in Python! It shows which code belongs to if or else.

# Another Example

# if_else.py

age = 18

if age >= 18:
    print("You can vote!")
else:
    print("You are too young to vote.")


# If age is 18 or more, it prints: You can vote!
# If age is less than 18, it prints: You are too young to vote.


# Tip:
# Use if-else whenever you want your program to choose between two options based on a condition.
