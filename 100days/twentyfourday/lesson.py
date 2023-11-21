# file = open("my_text.txt")
# contents = file.read()
# print(contents)
# file.close()

# with open("my_text.txt") as file:
#     contents = file.read()
#     print(contents)

# mode="a" == append
# mode="w" == write
# mode="r" == read
with open("my_text.txt", mode="a") as file:
    file.write("New text")
