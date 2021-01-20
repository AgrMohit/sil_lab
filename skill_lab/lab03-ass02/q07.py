num1 = float(input("enter a number: "))
num2 = float(input("enter another number: "))

if abs(num1 - num2) < 0.001:
    print("numbers are close")
else:
    print("numbers are not close")
