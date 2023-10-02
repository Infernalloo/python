# functions with inputs
def greet() :
    print("Hello ")
    print("World")
    print("!")
greet()

def greeting(name) :
 # parameter(argument)
    print(f"Hello {name}")
greeting("Alex")

def greet_with(name, location) :
    print(f"Hello {name}")
    print(f"What is it like in {location}")
# positional arguments
greet_with("Alex", "Italy")
# keyword arguments
greet_with(name="Alex", location="Italy")