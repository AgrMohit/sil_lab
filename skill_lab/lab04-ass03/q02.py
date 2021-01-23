import random

for i in range(1, 11):
    var1 = random.randint(1, 10)
    var2 = random.randint(1, 10)

    ans = int(input(f"Question {i}: {var1} x {var2} = "))

    if ans == var1 * var2:
        print("Right!")
    else:
        print(f"Wrong! Answer is {ans}")
