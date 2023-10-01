import random # import the random module
import os
# import the different variables from the modules
from hangman_art import stages
from hangman_art import logo
from hangman_words import word_list

print(logo) # print the logo for the game

game_over = False # sets if the game is over or not. Default if False
chosen_word = random.choice(word_list) # choose a random word from the list
word_length = len(chosen_word) # store the length of the random word
lives = 6 # declare how many lives 

display = [] # make a blank list
# append a '_' to the list, with length
# between 0 and the length of the random word
for blank in range(word_length) :
    display.append("_")


# while in the display list is at least one blank
# continue to loop
while not game_over :
    guess = input("Guess a letter:\n> ").lower() # ask the user for a letter and makes it lower case
    
    os.system("cls")

    # check if the user already guessed that word
    if guess in display :
        print("You already guessed this letter.")

    # we use range here so the variable position instead of a 
    # str gets a int, then we store the letter in the letter variable,
    # we compare the letter against the guess and if they are
    # the same, we change the blank to the letter
    for position in range(word_length) :
        letter = chosen_word[position]
        if letter == guess :
            display[position] = letter
            print(f"Lives: {lives}.")

    if guess not in chosen_word :
        print(f"The letter {guess} is not in the word.\n Lives: {lives}.")
        lives -= 1
        if lives == 0 :
            game_over = True
            print("You lost.")

    #Join all the elements in the list and turn it into a String.
    # just ctrl-c ctrl-v from the course, I still don't really 
    # understand much this line
    # I see that takes the list and puts the elements inside 
    # and converts it to a string, but not sure on syntax
    print(f"{' '.join(display)}")

    # check if there aren't any blanks in the list
    # if not, stop the game and win
    if "_" not in display :
        game_over = True
        print("You win.")

    print(stages[lives])