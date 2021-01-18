bs = float(input("enter basic salary: "))

ta = 20/100*bs
da = 120/100*bs
hra = 30/100*bs
gross = bs+ta+da+hra

print(f"basic salary: {bs}\nta: {ta}\nda: {da}\nhra: {hra}\ngross: {gross}")
