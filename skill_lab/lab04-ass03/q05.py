# Q05 - Use a for loop to print a box like the one below
# Allow the user to specify how wide and how high the box should be
# [Hint: print('*'*10) prints ten asterisks.]
# ********************
# ********************
# ********************
# ********************
# 01 - Mohit Raj
# 180310095

height = int(input("enter height of box: "))
width = int(input("enter width of box: "))

for i in range(height):
    for j in range(width):
        print('*', end=' ')
    print()
