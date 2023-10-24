# Randomisation
import random
# Import the random module
random_number = random.randint(1, 10)
print(random_number)
# nameOfTheModule.nameOfTheVariable()

random_float = round(random.random() * 5)
print(random_float)
# random.random() returns a number between
# 0 and 1, not including 1

# Modules
# Make the program in small modules
# import the name of the file in the main.py

# Lists
list = ["item1", "item2", 2, True]
print(list[3])
print(list[-4])

list.append() # append to the end of the list
list.extend() # extend a list with another list
# nested lists