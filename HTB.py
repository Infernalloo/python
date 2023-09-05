# var = "ABCDEF"
# print(var[:2])	# Up to index 2

# print(var[2:])	# Ignore everything up to index 2

# print(var[2:4])	# Everything between index 2 and 4 ("2" is counted)

# print(var[-2:])	# Up to negative index 2 (last two characters)


# favorite_colors = ["Orange", "Purple", "Blue"]

# for color in favorite_colors :
#     print(f"One of my favorite color is {color}")

    
# number = 0

# while number < 15 :
#     print(number)
#     number += 1

# list_1 = [5, 3, "Cake", True, 4, 5]
# index = 0

# for value in list_1 :
#     print(index)
#     index += 1

list_3 = ['Accidental', '4daa7fe9', 'eM131Me', 'Y!.90']
secret = []

for x in list_3:
    secret.append(x[:2])

print(''.join(secret))