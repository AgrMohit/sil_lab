import random

number = random.randint(1, 10)

guess = int(input("guess a number between 1 and 10: "))

if guess == number:
    print(f"you guessed right. number is {number}")
else:
    print(f"you guessed wrong. number is {number}")
