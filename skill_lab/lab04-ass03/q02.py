# Q02 - Kids Multiplication Table
# Write a multiplication game program for kids. The program should give
# the player ten randomly generated multiplication questions to do
# After each, the program should tell them whether they got it right or
# wrong and what the correct answer is
# 01 - Mohit Raj
# 180310095

import random

for i in range(1, 11):
    var1 = random.randint(1, 10)
    var2 = random.randint(1, 10)

    ans = int(input(f"Question {i}: {var1} x {var2} = "))

    if ans == var1 * var2:
        print("Right!")
    else:
        print(f"Wrong! Answer is {ans}")
