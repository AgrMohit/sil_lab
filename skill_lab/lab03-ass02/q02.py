# Q02 - Ask the user for a temperature. Then ask them what units, Celsius
# or Fahrenheit, the temperature is in. Your program should convert the
# temperature to the other unit. The conversions are
# F = 9 5C +32 and C = 5 9(F−32).
# 01 - Mohit Raj
# 180310095

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
