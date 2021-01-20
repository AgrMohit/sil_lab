len_in_cm = float(input("enter length in centimetres: "))

if len_in_cm < 0:
    print("number entered is invalid")
else:
    len_in_inch = len_in_cm / 2.54
    print(f"{len_in_cm} in inch: {len_in_inch}")
