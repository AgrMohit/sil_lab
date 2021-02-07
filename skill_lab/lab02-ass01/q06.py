# Q06 - Write a python program to input marks in 5 subjects of a student and
# print its average mark
# 01 - Mohit Raj
# 180310095

print("enter marks for 5 subjects:")

sum = 0.0
avg = 0.0
for marks in input().split():
    sum += float(marks)

avg = sum/5.0
print(f"average: {avg}")
