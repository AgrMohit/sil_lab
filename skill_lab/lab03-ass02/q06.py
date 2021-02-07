# Q06 - A store charges $12 per item if you buy less than 10 items
# If you buy between 10 and 99 items, the cost is $10 per item
# If you buy 100 or more items, the cost is $7 per item
# Write a program that asks the user how many items they are buying
# and prints the total cost
# 01 - Mohit Raj
# 180310095

number_of_items = int(input("how many items you are buying: "))

if number_of_items < 10:
    total_cost = 12 * number_of_items
elif number_of_items <= 99:
    total_cost = 10 * number_of_items
else:
    total_cost = 7 * number_of_items

print(f"total cost: {total_cost}")
