# Name:
# Class: 6th Hour
# Assignment: HW18

# 1. Import the random library and create a function that prints "Hello World!"
import random

def hello_world():
    print("Hello World!")


# 2. Create two empty integer variables named heads and tails
heads = 0
tails = 0


# 3. Create a function that flips a coin 100 times
def coin_flip():
    global heads, tails
    for i in range(100):
        flip = random.choice(["heads", "tails"])
        if flip == "heads":
            heads += 1
        else:
            tails += 1


# 4. Call the "Hello World" and "Coin Flip" functions
hello_world()
coin_flip()


# 5. Print the final result of heads and tails
print("Heads:", heads)
print("Tails:", tails)


# 6. Create a list called beanBag with at least 5 different colored beans
beanBag = ["red", "blue", "green", "yellow", "purple"]


# 7. Create a function that pulls a random bean and removes it
def pull_bean():
    if len(beanBag) > 0:
        bean = random.choice(beanBag)
        print("You pulled a", bean, "bean.")
        beanBag.remove(bean)
    else:
        print("The bean bag is empty.")


# 8. Create a function that asks if you want to pull another bean
def bean_pull():
    pull_bean()
    choice = input("Do you want to pull another bean? (yes/no): ")
    if choice.lower() == "yes":
        bean_pull()


# 9. Call the "Bean Pull" function
bean_pull()