# Q09 - Write a python program to compute SI and CI
# 01 - Mohit Raj
# 180310095

p = float(input("enter principal amount: "))
r = float(input("enter rate per annum: "))
t = float(input("enter time in years: "))

si = (p * r * t) / 100.0
ci_amt = p * pow((1 + r / 100), t)
ci = ci_amt - p

print(f"simple interest: {si}")
print(f"compound interest: {ci}")
