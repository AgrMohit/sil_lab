n = int(input("enter number till which to generate fibonacci sequence: "))

a = 0
b = 1

while a <= n:
    print(a, end=' ')
    c = a + b
    a = b
    b = c

print()
