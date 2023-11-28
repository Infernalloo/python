import random
from game_data import data
from art import logo
from art import vs
from os import clear

game_over = False
score = 0
data_length = len(data)
compares = []

compare_a = random.choice(data)

def higher_lower():

    global game_over
    global score
    global compare_a
    
    compare_b = random.choice(data)

    print(logo)
    print(f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}")
    print(vs)
    print(f"Compare B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}")

    user_guess = input("Choose between A and B: ").lower()
    if user_guess == "a":
        if compare_a['follower_count'] > compare_b['follower_count']:
            print("You guessed right!")
            score += 1
            clear()
        elif compare_a['follower_count'] < compare_b['follower_count']:
            print("You lost!")
            game_over = True
    elif user_guess == "b":
        if compare_b['follower_count'] > compare_a['follower_count']:
            print("You guessed right!")
            score += 1
            clear()
        elif compare_b['follower_count'] < compare_a['follower_count']:
            print("You lost!")
            game_over = True

    print(f"You score is {score}.")
    compare_a = compare_b


while not game_over :
    higher_lower()
    