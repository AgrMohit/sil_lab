temp = float(input("enter temperature: "))
unit = input("what unit is the temperature in (c/f): ")

if unit != 'c' and unit != 'f':
    print("invalid unit")
else:
    if unit == 'c':
        f = (9 * temp / 5) + 32
        print(f"temperature in fahrenheir: {f}")
    elif unit == 'f':
        c = (temp - 32) * 5 / 9
        print(f"temperature in celsius: {c}")
