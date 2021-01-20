credits = int(input("enter number of credits you have taken: "))

if credits <= 23:
    print("student is a freshman")
elif credits <= 53:
    print("student is a sophomore")
elif credits <= 83:
    print("student is a junior")
else:
    print("student is a senior")
