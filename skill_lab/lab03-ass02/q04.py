# Q04 - Write a program that asks the user how many credits they have taken
# If they have taken 23 or less, print that the student is a freshman
# If they have taken between 24 and 53, print that they are a sophomore
# The range for juniors is 54 to 83, and for seniors it is 84 and over
# 01 - Mohit Raj
# 180310095

credits = int(input("enter number of credits you have taken: "))

if credits <= 23:
    print("student is a freshman")
elif credits <= 53:
    print("student is a sophomore")
elif credits <= 83:
    print("student is a junior")
else:
    print("student is a senior")
