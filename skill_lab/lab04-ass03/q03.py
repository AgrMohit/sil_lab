# Q03 - Check a list contains even number or not
# numbers = [11,33,55,39,55,75,37,21,23,41,13]
# 01 - Mohit Raj
# 180310095

numbers = [11, 33, 55, 39, 55, 75, 37, 21, 23, 41, 13]

print(numbers)

for number in numbers:
    if number % 2 == 0:
        print('list contains an even number')
        break

print('list does not contain an even number')
