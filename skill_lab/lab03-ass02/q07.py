# Q07 - Write a program that asks the user for two numbers and prints
# Close if the numbers are within .001 of each other and Not close otherwise
# 01 - Mohit Raj
# 180310095

num1 = float(input("enter a number: "))
num2 = float(input("enter another number: "))

if abs(num1 - num2) < 0.001:
    print("numbers are close")
else:
    print("numbers are not close")
