import random

number = random.randint(1, 100)
while True:
    i = int(input("Pick a number between 1 and 100: "))
    if i == number:
         print("You win!")
         break
    elif i >= number:
         print("Your number is too high")
    elif i <= number:
         print("Your number is too low")