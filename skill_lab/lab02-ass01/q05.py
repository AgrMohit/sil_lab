# Q05 - Write a python program to input the radius of a circle and print
# its area and perimeter
# 01 - Mohit Raj
# 180310095

import math
radius = float(input("enter radius of circle: "))

area = math.pi * radius ** 2
perimeter = 2 * math.pi * radius

print(f"area: {area}")
print(f"perimeter: {perimeter}")
