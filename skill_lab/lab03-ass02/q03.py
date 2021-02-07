# Q03 - Ask the user to enter a temperature in Celsius. The program should
# print a message based on the temperature: If the temperature is less than
# -273.15, print that the temperature is invalid because it is below absolute zero
# • If it is exactly -273.15, print that the temperature is absolute 0
# • If the temperature is between- 273.15 and 0, print that the temperature is below freezing
# • If it is 0, print that the temperature is at the freezing point
# • If it is between 0 and 100, print that the temperature is in the normal range
# • If it is 100, print that the temperature is at the boiling point
# • If it is above 100, print that the temperature is above the boiling point
# 01 - Mohit Raj
# 180310095

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
