# Q04 - Write a python program to input the basic salary of a person and
# compute its TA (20% of basic), DA (120% of basic), HRA (30% of basic),
# Gross (basic + ta + da + hra)
# 01 - Mohit Raj
# 180310095

bs = float(input("enter basic salary: "))

ta = 20/100*bs
da = 120/100*bs
hra = 30/100*bs
gross = bs+ta+da+hra

print(f"basic salary: {bs}\nta: {ta}\nda: {da}\nhra: {hra}\ngross: {gross}")
