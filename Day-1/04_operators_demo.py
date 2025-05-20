# Basic Operators


# Arithmetic Operators:{

# +   Addition
# -   Subtraction
# *   Multiplication
# /   Division
# %   Modulus (remainder)
# **  Exponent (power)

# }


# Comparison Operators:{

# ==  Equal
# !=  Not Equal
# >   Greater than
# <   Less than
# >=  Greater or equal
# <=  Less or equal

# }


# Logical Operators:{

# and   # Dono condition true ho to true
# or    # Kisi ek true ho to true
# not   # Opposite karega (True → False)

# }

# ab hum ise simple lenguage me samaj te hai fir aek chhota sa project bana ye ge jisse ye topic esay lage ga 


# Arithmetic Operators (Short Summary with Examples):

a = 10
b = 3

print("Addition (a + b):", a + b)         # 13
print("Subtraction (a - b):", a - b)      # 7
print("Multiplication (a * b):", a * b)   # 30
print("Division (a / b):", a / b)         # 3.333...
print("Modulus (a % b):", a % b)          # 1
print("Exponent (a ** b):", a ** b)       # 1000  (10*10*10=1000)


# ye samaj aa gaya na ab ham Comparison Operators samaj te hai 


# Comparison Operators (Short Summary with Examples):




x = 5
y = 8

print("Equal (x == y):", x == y)           # False
print("Not Equal (x != y):", x != y)       # True
print("Greater than (x > y):", x > y)      # False
print("Less than (x < y):", x < y)         # True
print("Greater or equal (x >= y):", x >= y) # False
print("Less or equal (x <= y):", x <= y)    # True


# ertainly! Here’s a short explanation for each comparison operator in your code:

# == (Equal): Checks if two values are the same.
# Example: x == y is False because 5 is not equal to 8.

# != (Not Equal): Checks if two values are different.
# Example: x != y is True because 5 is not equal to 8.

# > (Greater than): Checks if the left value is bigger than the right.
# Example: x > y is False because 5 is not greater than 8.

# < (Less than): Checks if the left value is smaller than the right.
# Example: x < y is True because 5 is less than 8.

# >= (Greater or equal): Checks if the left value is bigger or equal to the right.
# Example: x >= y is False because 5 is not greater than or equal to 8.

# <= (Less or equal): Checks if the left value is smaller or equal to the right.
# Example: x <= y is True because 5 is less than or equal to 8.

# These operators are used to compare values and return True or False.



# Logical Operators in Python:

# 1. and
#   - Tabhi True deta hai jab dono conditions True ho.
#   - Example:
a = 5
b = 10
print(a > 2 and b < 15)  # Output: True (kyunki dono conditions true hain)
print(a > 2 and b > 15)  # Output: False (kyunki dusri condition false hai)

# 2. or
#   - Kisi bhi ek condition True ho to result True aata hai.
#   - Example:
print(a > 2 or b > 15)   # Output: True (kyunki pehli condition true hai)
print(a < 2 or b > 15)   # Output: False (dono hi false hain)

# 3. not
#   - Condition ka result ulta kar deta hai (True ko False, False ko True).
#   - Example:
x = True
print(not x)             # Output: False (kyunki x True tha)
print(not (a > 2))       # Output: False (kyunki a > 2 True hai, not lagane se False ho gaya)

# Note:
# - 'and' tabhi True deta hai jab dono conditions True ho.
# - 'or' tabhi False deta hai jab dono conditions False ho.
# - 'not' result ko ulta kar deta hai.



# ab bat rahi project ki to hum pehle if else ko samaj lete hai fir frist project hum done kar denge 