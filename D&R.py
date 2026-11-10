import random

secret_number = random.randint(1,20)
attempts = 0
guess = 0
print(f'Hello Welcome to the Number Game!!')
print(f"You are going to guess a number between 1 and 20")
print(f"And every guess you attempt will be added and one ")
print(f'And you be told if the number you guessed is higher or lower than the correct number')

while guess != secret_number:
    guess = int(input('Enter your guess: '))
    attempts += 1
    if guess < secret_number:
        print('Your guess is too low')
    if guess > secret_number:
        print('Your guess is too high')
    else:
        print('You got the Number!!')
        print(f'You attempted {attempts} times')
