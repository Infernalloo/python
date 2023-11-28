PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names:
    names_list = names.readlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    letter_contents = letter.read()
    for name in names_list:
        stripped_name = name.strip("\n")
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as finished_letters:
            finished_letters.write(new_letter)
