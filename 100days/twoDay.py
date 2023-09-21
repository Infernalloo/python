# Primitive data types
string = "This is a string"
character = string[8] # This is called subscripting
integer = 123_456_789 # Used underscores instead of comma, the computer is going to ignore it
float = 6.9
boolean = True

# Type func
type(boolean)

# Type conversion or type casting
str(integer)
int(float)

# Math operators
# PEMDAS
1 + 2
2 - 1
4 * 4
6 / 3
2 ** 4
5 % 2

# Round func
round(6 / 4, 3) # round the number after 3 numbers

# Floor division
5 // 3 # return a float with 2 decimals

# F strings
print(f"The score is {integer}")