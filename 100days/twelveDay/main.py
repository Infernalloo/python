import random
from logo_ascii import logo


def game():
    print(logo)
    random_number = random.randint(1, 100)
    game_over = False
    lives = 0

    user_difficulty = input("You can choose easy or hard difficulty.\n> ")
    if user_difficulty == "easy":
        lives = 10
    elif user_difficulty == "hard":
        lives = 5
    else:
        print("Did you make a typo?")
    print(f"You have {lives} turns. Try your best!")

    while not game_over and lives > 0:
        user_guess = int(input("Guess a number between 1 and 100.\n> "))

        if user_guess == random_number:
            print(f"You guessed right! The number was {random_number}")
            game_over = True
        elif user_guess > random_number:
            print("Too high. Try again")
            lives -= 1
        elif user_guess < random_number:
            print("Too low. Try again")
            lives -= 1
        else:
            print("Did you make a typo?")

    print(f"Sorry, you lost. The number was {random_number}")


game()