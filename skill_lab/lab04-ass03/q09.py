word = input("enter a word: ")

length = len(word)
flag = -1

for i in range(0,  int(length/2)):
    if i % 2 == 0:
        if word[i] < word[length - 1 - i]:
            flag = 1
        else:
            flag = 0
            break
    else:
        if word[i] > word[length - 1 - i]:
            flag = 1
        else:
            flag = 0
            break

if flag == 0:
    print("not a magic word")
elif flag == 1:
    print("magic word")
