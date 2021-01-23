import random

# +ve score = user
# -ve score = computer
score = 0

for i in range(5):
    user = input('rock, paper or scissor: ')
    computer = random.choice(['rock', 'scissor', 'paper'])

    if user == 'rock':
        if computer == 'rock':
            pass
        elif computer == 'paper':
            score -= 1
        else:  # scissor
            score += 1
    elif user == 'paper':
        if computer == 'rock':
            score += 1
        elif computer == 'paper':
            pass
        else:  # scissor
            score -= 1
    elif user == 'scissor':
        if computer == 'rock':
            score -= 1
        elif computer == 'paper':
            score += 1
        else:  # scissor
            pass
    else:
        print("invalid input. try again")
        i -= 1
        continue

    print(f"you: {user}\ncomputer: {computer}")

if score < 0:
    print(f"computer won by {0-score} points")
elif score > 0:
    print(f"you won by {score} points")
else:
    print("game was a tie")
