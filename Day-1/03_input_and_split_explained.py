# NOTE: Input from User in Python and split() function 

# Basic Explanation:
# In Python, you can take input from the user using the built-in `input()` function.
# This function pauses the program and waits for the user to type something and press Enter.
# The value returned by `input()` is always a string.

# Example 1: Taking a simple input
name = input("Enter your name: ")
print("Hello,", name)

# Example 2: Taking numeric input
# Since input() returns a string, you need to convert it to int or float if you want numbers.
age = int(input("Enter your age: "))
print("You are", age, "years old.")

# Example 3: Taking multiple inputs in one line
# You can use split() to take multiple values at once.
# niche diye gaye split() function ko ham last me dekhe ge ki kese kam kar ta hai abhi sirf use karo baki idia niche dekh ke samaj na ok
x, y = input("Enter two numbers separated by space: ").split()
print("First number:", x)
print("Second number:", y)

# Example 4: Converting multiple inputs to integers
a, b = map(int, input("Enter two integers: ").split())
print("Sum:", a + b)

# Advanced: Customizing input prompts and error handling

# yaha pe bhi if else ka use kiya gaya hai vo bhi ek python ka function hai hum use next time pura samje ge kyu ki vo bahut jaruri hai to abhi dekho ham uska use bad me achhe se samje ge 

marks = float(input("Enter your marks (out of 100): "))
if 0 <= marks <= 100:
    print("Your marks are:", marks)
else:
  print("Marks should be between 0 and 100.")


# Summary Notes:
# - input() always returns a string.
# - Use int(), float(), etc. to convert input to numbers.
# - Use split() and map() for multiple inputs.
# - Always handle errors using try-except for robust code.



# to split function ko hum samaj te hai pura 

# 🔹 Basic Idea:
# split() function ek string ko parts mein tod deta hai, jise hum "list" ke roop mein paate hain. Yeh mainly kisi separator (jaise space, comma, etc.) ke basis par string ko todta hai.

# ---

# Syntax:
# ```python
# string.split(separator, maxsplit)
# ```

# eparator (optional): Jis character ya word ke base par string ko todna hai. Agar nahi doge to default space (' ') hoga.
# maxsplit (optional): Kitni baar todna hai. Agar nahi doge to jitni baar ho sake tod dega.

# ---

# Tumhare Code ka Explanation:
# ```python
# x, y = input("Enter two numbers separated by space: ").split()
# ```

# Step-by-step:
# 1. input() user se ek string input leta hai.
# Example: "10 20"

# 2. .split() is string ko space (' ') ke base par do parts mein todta hai:
#    ```python
#    ["10", "20"]
#    ```

# 3. x, y  yeh list ke pehle aur doosre element ko x aur y mein assign kar deta hai.
#    x = "10"  
#    y = "20"

# 4. print() dono values ko print karta hai:
#    ```
#    First number: 10
#    Second number: 20
#    ```

# ---

# Examples of split() with different separators:

# 1. Space se split karna:
# ```python
# text = "hello world"
# words = text.split()
# print(words)  # ['hello', 'world']
# ```

# 2. Comma (`,`) se split karna:
# ```python
# data = "apple,banana,cherry"
# fruits = data.split(",")
# print(fruits)  # ['apple', 'banana', 'cherry']
# ```

# 3. Maximum split limit lagana:
# ```python
# line = "one two three four"
# parts = line.split(" ", 2)
# print(parts)  # ['one', 'two', 'three four']
# ```

# ---

# Real Life Use Case:
# CSV files read karte waqt
# User input ko process karte waqt
# Text parsing ya data cleaning ke waqt
# Log files analyse karne mein

# ---

#  Summary in Easy Hindi:
#  split() ek string ko chhote tukdon mein baantta hai.
#  Default separator space hota hai.
#  Result hamesha "list" mein milta hai.
#  Har tukda string hi hota hai, number banana ho to int() ya float() ka use karte hain.

# ---

# Extra Tip:
# Agar number chahiye toh:
# ```python
# x, y = map(int, input("Enter two numbers: ").split())
# ```
# Ab x aur y directly int ban jaayenge.

# ---
