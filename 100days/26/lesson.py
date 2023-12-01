# List comprehension
# new_list = [new_item for item in list]

# Conditional List Comprehension
# new_list = [new_item for item in list if test]

numbers = [1, 2, 3]
new_numbers = [number * 2 for number in numbers]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_name = [name for name in names if len(name) < 5]
uppercase_name = [name.upper() for name in names if len(name) >= 5]
print(uppercase_name)
