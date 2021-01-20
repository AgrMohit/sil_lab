number_of_items = int(input("how many items you are buying: "))

if number_of_items < 10:
    total_cost = 12 * number_of_items
elif number_of_items <= 99:
    total_cost = 10 * number_of_items
else:
    total_cost = 7 * number_of_items

print(f"total cost: {total_cost}")
