# Q04 - Read N and generate the Fibonacci sequence upto N
# 01 - Mohit Raj
# 180310095

n = int(input("enter number till which to generate fibonacci sequence: "))

a = 0
b = 1

while a <= n:
    print(a, end=' ')
    c = a + b
    a = b
    b = c

print()
