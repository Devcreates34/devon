import random

def game():
    computer = random.randint(1,3)
    user = int(input("Pick 1 for Rock, 2 for Paper, or 3 for Scissors: "))

    if user == 1:
        print("You picked Rock")
    elif user == 2:
        print("You picked Paper")
    elif user == 3:
        print("You picked Scissors")
    else:
        print("Pick a valid number.")
        return

    if computer == 1:
        print("Computer picked Rock")
    elif computer == 2:
        print("Computer picked Paper")
    elif computer == 3:
        print("Computer picked Scissors")

    if user == computer:
        print("Tie!!")
    elif (user == 1 and computer == 3) or (user == 2 and computer == 1) or (user == 3 and computer == 2):
        print("You Win!!")
    else:
        print("You Lose!!")


def play_game():
    while True:
        game()
        again = input("Do you want to play again? (y/n): ").lower()
        if again != "y":
            print("Thank you for playing!")
            break

play_game()