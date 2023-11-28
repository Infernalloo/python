import os
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
print("Welcome to the Blind Auction System.")

auction_contestant = {}
finish_loop = False

def price_comparison(bidding_list) :
    highest_bid = 0
    winner = ""
    for bid in bidding_list :
        price = bidding_list[bid]
        if price > highest_bid :
            highest_bid = price
            winner = bid
    print(f"The winner is {winner} with ${highest_bid}.")

while not finish_loop:

    name = input("What is you name?\n> ")
    bid = int(input("How much do you want to bid?\n> "))
    auction_contestant[name] = bid

    other_people = input("More doods? Yes or No?\n> ").lower()
    if other_people == "yes" :
        os.system('clear')
    elif other_people == "no" :
        os.system('clear')
        finish_loop = True
        price_comparison(auction_contestant)

