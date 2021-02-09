# Q09 - Playing with Magic Words
# Here a word 'S' of length 'n is said to be magic word if it satisfies:
# All letters of S are lowercase letters of the English alphabets.
# Si, the character in the ith position, is lexicographically smaller than
# Sn-1-i for all even i from 0 to n/2
# Si is lexicographically greater than Sn-1-i for all odd i from 0 to n/2
# For example, the word 'difference' is a magic word, while 'similar' is not
# Given a word, write python code to check whether the word is magic or not
# 01 - Mohit Raj
# 180310095

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
    print(f" {word} is not a magic word")
elif flag == 1:
    print(f"{word} is a magic word")
