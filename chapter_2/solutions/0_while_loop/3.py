""" 
Exercise 3: Guess the Number
-Generate a random number between 1 and 100.
-Ask the user to guess the number.
-Use a while loop to keep asking the user for a guess until they guess the correct number.
-Give hints if the guess is too high or too low.
"""

import random 

secret_number = random.randint(1, 100)
guess = int(input("Guess a number between 1 and 100: "))

while guess != secret_number:
    if guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    guess = int(input("Guess a number between 1 and 100: "))

print("Congratulations! You guessed the number correctly!")
