# Q02 - Write a python program to input two number and swap their values
# without using any third variable
# 01 - Mohit Raj
# 180310095

a = int(input("enter first number: "))
b = int(input("enter second number: "))

a, b = b, a

print(f"a: {a}\tb:{b}")
