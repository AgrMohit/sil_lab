# Q08 -Write a python program to input a the sides of a triangle and
# print its area
# 01 - Mohit Raj
# 180310095

import math
print("enter sides of triangle: ")


res = input().split()
a, b, c = float(res[0]), float(res[1]), float(res[2])
s = (a + b + c) / 2.0

area = math.sqrt(s * (s - a) * (s-b) * (s - c))
print(f"area: {area}")
