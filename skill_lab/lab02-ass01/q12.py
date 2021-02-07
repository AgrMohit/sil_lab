# Q12 - Write a python program to evaluate the expression
# 4x^4 + 3y^3 -9z + 6
# 01 - Mohit Raj
# 180310095

print("expression: 4x^4 + 3y^3 - 9z + 6")

x = float(input("enter value of x: "))
y = float(input("enter value of y: "))
z = float(input("enter value of z: "))

res = 4 * pow(x, 4) + 3 * pow(y, 3) - 9 * z + 6

print(f"result of expression: {res}")
