 
import random # import the random module
word_list = ["aardvark", "baboon", "camel"] # declare the list of the words used

# list with all the ascii art for the different stages of the game.
# changes in base of how many lives are left
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

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
    
    # we use range here so the variable position instead of a 
    # str gets a int, then we store the letter in the letter variable,
    # we compare the letter against the guess and if they are
    # the same, we change the blank to the letter
    for position in range(word_length) :
        letter = chosen_word[position]
        if letter == guess :
            display[position] = guess

print(display)