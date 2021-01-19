a = int(input("enter first number: "))
b = int(input("enter second number: "))

# method 1
a, b = b, a

# method 2
# a = a + b
# b = a - b
# a = a - b

print(f"a: {a}\tb:{b}")
