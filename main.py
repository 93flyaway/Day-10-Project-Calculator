#Calculator

#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

#format float number
def format_decimal(float_value):
    result = "{:.2f}".format(float_value)
    return result

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
from art import logo

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    should_continue = True

    while should_continue:
        for operator in operations:
            print(operator)
        operator_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the second number?: "))
        calculation_function = operations[operator_symbol]
        answer = format_decimal(round(calculation_function(num1, num2), 2))
        print(f"{num1} {operator_symbol} {num2} = {answer}")
        
        if input("Type 'y' to continue, and type 'n' to exit: ") == 'y':
            num1 = float(answer)
        else:
            should_continue = False
    calculator()

calculator()