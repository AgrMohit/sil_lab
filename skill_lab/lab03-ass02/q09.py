# Q09 - Write a program that asks the user for an hour between 1 and 12, asks
# them to enter am or pm, and asks them how many hours into the future they want to go
# Print out what the hour will be that many hours into the future, printing am or pm
# as appropriate. An example is shown below.
# Enter hour: 8 am How many hours ahead? 5 New hour: 1 pm
# 01 - Mohit Raj
# 180310095

hour = int(input("enter hour between 1 and 12: "))
am_or_pm = input("enter am or pm: ")
hours_into_future = int(
    input("how many hours into future do you want to go: "))

new_am_or_pm = ''
new_hour = (hour + hours_into_future) % 12

if int((hour + hours_into_future) / 12) % 2 == 0:
    new_am_or_pm = am_or_pm
else:
    if am_or_pm == 'am':
        new_am_or_pm = 'pm'
    elif am_or_pm == 'pm':
        new_am_or_pm = 'am'
    else:
        print("invalid time")
        exit(1)

print(f"time {hours_into_future} hours in future: {new_hour} {new_am_or_pm}")
