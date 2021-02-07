# Q11 - Write a python program to swap three variables
# 01 - Mohit Raj
# 180310095

a = int(input("enter number 1: "))
b = int(input("enter number 2: "))
c = int(input("enter number 3: "))

print(f"a: {a}\nb: {b}\nc: {c}")
print("swapping values")

a, b, c = b, c, a

print(f"a: {a}\nb: {b}\nc: {c}")
