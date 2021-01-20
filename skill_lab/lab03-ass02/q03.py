temp = float(input("enter temperature in celsius: "))

if temp < 273.15:
    print("temperature in invalid as it is below absolute zero")
elif temp == 273.15:
    print("temperature is absolute zero")
elif temp <= 0:
    print("temeperature is below freezing")
elif temp < 100:
    print("temperature is in normal range")
else:
    print("temperature is above boiling point")
