import math

num = int(input("enter value of n: "))
sum = 0.0

for i in range(1, num+1):
    sum += 1/math.factorial(i)

print(f"sum: {sum}")
