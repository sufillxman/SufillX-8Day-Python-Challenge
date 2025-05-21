import random
# import random is ko laga na jaruri hai tabhi  random.randint(1, 100)ye code kam kare ga 

print("="*50)
# upar vali line sirf lain bana ti hai nahi likho ge to bhi chale ga

print(" Welcome to the Number Guessing Game!")
print("="*50)
#  ye bhi vesa hi kam kar ti hai 

print("I'm thinking of a number between 1 and 100.")
print("Can you guess what it is? Let's find out!\n")

# Computer ek random number choose karega
#  random number ka consept samaj na aye to bata na me iske liye alag se file bana ke samja dunga 

secret_number = random.randint(1, 100)
attempts = 0

while True:
    user_input = input(" Enter your guess (1 to 100): ")

    # Check karenge input valid number hai ya nahi
    if not user_input.isdigit():
        print(" Please enter a valid number!\n")
        continue

    guess = int(user_input)

    if guess < 1 or guess > 100:
        print(" Number must be between 1 and 100.\n")
        continue

    attempts += 1

    if guess < secret_number:
        print(" Too low! Try again.\n")
    elif guess > secret_number:
        print(" Too high! Try again.\n")
    else:
        print(f" Congratulations! You guessed the number in {attempts} attempts.")
        break

print("\n Thank you for playing the Guessing Game!")
