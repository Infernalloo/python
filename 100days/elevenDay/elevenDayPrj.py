import random
from os import clear
from art import logo


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    random_card = random.choice(cards)
    return random_card


def calculate_score(cards):
    summed_cards = sum(cards)

    if summed_cards == 21 and len(cards) == 2:
        return 0

    if 11 in cards and summed_cards > 21:
        cards.remove(11)
        cards.append(1)

    return summed_cards


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a draw"
    elif computer_score == 0:
        return "Dealer wins"
    elif user_score == 0:
        return "User wins"
    elif user_score > 21:
        return "Dealer wins"
    elif computer_score > 21:
        return "Dealer loses"
    elif user_score > computer_score:
        return "User wins"
    elif user_score < computer_score:
        return "Dealer wins"
    else:
        return "There was an error. Sorry :)"


def blackjack() :
    print(logo)
    
    game_over = False
    user_cards = []
    computer_cards = []
    for card in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    print(f"Your cards are : {user_cards}")
    print(f"Dealer's first card is : {computer_cards[0]}")

    
    while not game_over:
    
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
    
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            continue_game = input("Do you want to draw another card?\n> ").lower()
            if continue_game == "no":
                game_over = True
            else:
                user_cards.append(deal_card())
                print(f"Your cards are : {user_cards}")
                if computer_score < 17:
                    computer_cards.append(deal_card())


    print(f"Your cards are : {user_cards}, the dealer cards are : {computer_cards}.")
    compare(user_score, computer_score)


restart = input("Do you want to play another match? Yes or No?").lower()

while restart == "y" :
    clear()
    blackjack()


