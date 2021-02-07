# Q01 - Write a program that asks the user to enter a length in centimetres.
# If the user enters a negative length, the program should tell the user that
# the entry is invalid. Otherwise, the program should convert the length to
# inches and print out the result. 1inch = 2.54 centimetres
# 01 - Mohit Raj
# 180310095

len_in_cm = float(input("enter length in centimetres: "))

if len_in_cm < 0:
    print("number entered is invalid")
else:
    len_in_inch = len_in_cm / 2.54
    print(f"{len_in_cm} in inch: {len_in_inch}")
