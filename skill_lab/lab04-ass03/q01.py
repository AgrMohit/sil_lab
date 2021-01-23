import random

number = random.randint(1, 5)
guess = int(input("enter a number between 1 and 5 (both inclusive): "))

if guess == number:
    print("you guessed right")
else:
    print(f"you guessed wrong. number: {number}")
