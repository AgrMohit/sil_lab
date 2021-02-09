# Q06 - Use loop to print a box like the one below
# Allow the user to specify how wide and how high the box should be
# ********************
# *                  *
# *                  *
# ********************
# 01 - Mohit Raj
# 180310095

height = int(input("enter height of the box: "))
width = int(input("enter width of the box: "))

for i in range(height):
    if i == 0 or i == height-1:
        for j in range(width):
            print('* ', end='')
        print()
    else:
        print('* ', end='')
        for j in range(width-2):
            print('  ', end='')
        print('* ')
