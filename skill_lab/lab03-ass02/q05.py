# Q05 - Generate a random number between 1 and 10. Ask the user to guess
# the number and print a message based on whether they get it right or not
# 01 - Mohit Raj
# 180310095

import random

number = random.randint(1, 10)

guess = int(input("guess a number between 1 and 10: "))

if guess == number:
    print(f"you guessed right. number is {number}")
else:
    print(f"you guessed wrong. number is {number}")
