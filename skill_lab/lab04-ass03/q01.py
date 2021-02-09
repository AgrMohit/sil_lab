# Q01 - Guess a number game
# The computer picks a random number from 1 to 5, the player tries
# to guess. The player may have the flexibility to enter the number
# in an expression format.
# 01 - Mohit Raj
# 180310095

import random

number = random.randint(1, 5)
guess = int(input("enter a number between 1 and 5 (both inclusive): "))

if guess == number:
    print("you guessed right")
else:
    print(f"you guessed wrong. number: {number}")
