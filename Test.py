import random

cards_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4

def calculate_total(hand):
    total = sum(hand)
    aces = hand.count(11)

    while total > 21 and aces:
        total -= 10
        aces -= 1

    return total

def card_play():
    player_hand = [random.choice(cards_list), random.choice(cards_list)]
    dealer_hand = [random.choice(cards_list), random.choice(cards_list)]

    player_total = calculate_total(player_hand)
    dealer_total = calculate_total(dealer_hand)

    print("Dealer hand:", dealer_hand, "Total:", dealer_total)
    print("Player hand:", player_hand, "Total:", player_total)

    if dealer_total != 21 and player_total < 21:
        x = str(input('Would you like to hit(h) or stand(s)?: '))
        if x == 'h':
            y = player_total + random.choice(cards_list)
            print(y)


    if player_total == 21 and dealer_total == 21:
        print("Both Player and Dealer Blackjack, Tie!!")
    elif dealer_total == 21:
        print("Dealer Blackjack!! You lose")
    elif player_total == 21:
        print("Player Blackjack!! You win")

card_play()