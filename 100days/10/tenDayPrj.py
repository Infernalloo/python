from art import logo

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator() :
    print(logo)
    num1 = float(input("Wha's the first number?: "))
    
    for operator in operations :
        print(operator)
    
    stop_calculator = False
    while not stop_calculator :
        operation_symbol = input("Pick an operation: ")
        
        num2 = float(input("What's the next number?: "))
        
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
    
        continue_calculator = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ").lower()
    
        if continue_calculator == "y" :
            num1 = answer
        else :
            stop_calculator = True
            calculator()
    
        print(f"{num1} {operation_symbol} {num2} = {answer}")

calculator()