print("enter marks for 5 subjects:")

sum = 0.0
avg = 0.0
for marks in input().split():
    sum += float(marks)

avg = sum/5.0
print(f"average: {avg}")
