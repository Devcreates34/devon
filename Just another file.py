import random

win = 0
lose = 0
tie = 0

# run the game 1000 times
for _ in range(1000):
    computer = random.randint(1, 3)  # 1=rock, 2=paper, 3=scissors
    rock_user = 1  # user always chooses rock

    if rock_user == 1 and computer == 3:
        win += 1
    elif computer == rock_user:
        tie += 1
    elif rock_user == 1 and computer == 2:
        lose += 1

print("The Rock user won", win, "times")
print("The Rock user lost", lose, "times")
print("The Rock user tied", tie, "times")