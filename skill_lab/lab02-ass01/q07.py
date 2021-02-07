# Q07 - Write a python program to input a number and print its square,
# cube and fourth power
# 01 - Mohit Raj
# 180310095

import math
base = int(input("enter a number: "))

print(
    f"square: {base*base}\ncube: {math.pow(base, 3)}\nfourth power: {math.pow(base, 4)}")
