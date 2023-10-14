# functions with outputs
def my_function() :
    result = 4 * 2
    return result
def better_function() :
    return 4 * 2

def format_name(f_name, l_name) :
    """This is a docstring. Small documentation for functions.
    Can be used even as multi line comment."""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

formated_string = format_name("Alex", "BIaNu")
print(formated_string)

# To remember
def is_leap(year) :
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
  
def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  if month == 2 and is_leap(year) == True :
    return 29
  else :
    return month_days[month - 1]

year = int(input())
month = int(input())
days = days_in_month(year, month)
print(days)

