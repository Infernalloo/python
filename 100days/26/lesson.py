import random
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

# Dictionary Comprehension
# Creating a new dict from a list
# new_dict = {new_key:new_value for item in list}
# Creating a new dict form an existing dict
# new_dict = {new_key:new_value for (key,value) in dict.items()}

# Conditional dictionary comprehension
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}

students_scores = {student:random.randint(1, 100) for student in names}
print(students_scores)

passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)