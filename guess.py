#Random number guessing game

import random

secret_num = random.randint(1, 100)

guess = int(input("Guess the number between 1 and 100: "))

while guess != secret_num:
    if guess > secret_num:
        guess = int(input(f"{guess} is too high! Guess the number between 1 and 100: "))
    elif guess < secret_num:
        guess = int(input(f"{guess} is too low! Guess the number between 1 and 100: "))
else:
    print(f"Correct! The number is {secret_num}!")