import random
LOWER_LIMIT=0
UPPER_LIMIT= 100
random_number = random.randint(LOWER_LIMIT, UPPER_LIMIT)
print ("The computer has selected a number between 0 and 100. " \
       "Use your supernatural superpowers to guess what the number is.")
while True:
    user_guess = int(input("Enter a number between 0 and 100 (including): "))
    if user_guess > random_number:
        print("Guess a smaller number.")
    elif user_guess < random_number:
        print("Guess a larger number.")
    else: #user_guess == random_number:
        print("You Won!")
        break
