#  Basic login system created by Sufill X Man

#  Step 1: Ask for username and password
'''
username = input("Enter your username: ")
password = input("Enter your password: ")

'''

# Step 2: Check if the entered credentials are correct
'''
if username == "sufill" and password == "python123":
    print("Login successful! Welcome back, Sufill!")
else:
    print("Invalid username or password. Please try again.")

'''
#  Is code se kya seekhega?
# Concept	Explanation
# input()	User se username & password lena
# if & and	Dono condition match hone par hi login allow
# String comparison	Username aur password match check karna

#  Output Example:
# Enter your username: sufill
# Enter your password: python123
#  Login successful! Welcome back, Sufill!

# Enter your username: wrong
# Enter your password: 1234
# Invalid username or password. Please try again.
# Bonus: Advance idea (optional future update)

# # List of users (for future)
# users = {
#     "sufill": "python123",
#     "admin": "adminpass"
# }
# Bhai ab tu is login_system.py ko:



# Here are 3 different examples using  and, or, not statements in Python, each with a real-life scenario:
'''

# Example 1: Age + Country Based Login System
# “Sirf Indian users jinki age 18+ hai, unko login milta hai”

# Login system based on age and country - by Sufill X Man

# Step 1: Get user details
name = input("Enter your name: ")
age = int(input("Enter your age: "))
country = input("Enter your country: ")

# Step 2: Check eligibility
if age >= 18 and country.lower() == "india":
    print(f" Welcome {name}! You are eligible to access the system.")
else:
    print("Access Denied! You must be 18+ and from India.")
Operators used: >=, and, .lower()

'''

# Example 2: Username Check with or
# “Login allow ho agar user sufill ya admin ho”


#  Allow specific usernames - Sufill's simple filter
'''
username = input("Enter your username: ")
'''
# # Allow only specific users
'''
 if username == "sufill" or username == "admin":
     print("Welcome, you are an authorized user!")
 else:
     print("Access denied! Unauthorized username.")

'''
# Operators used: ==, or


#  Example 3: not Operator – Reversed Logic
# “Login tabhi allow ho jab user blocked list me nahi ho”

# Blocked user check - by Sufill
'''
blocked_users = ["hacker123", "spammer", "banned_user"]

username = input("Enter your username: ")

if username not in blocked_users:
    print(f"Access granted to {username}. Welcome!")
else:
    print("You are blocked. Access denied.")

'''
# Operators used: not in, list, if-else
