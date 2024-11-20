from art import logo
print(logo)
# TODO: Write out the other 3 functions - subtract, multiply and divide.
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2 

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2
# TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"
operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
# TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.
# operation_calc = operation["*"](4, 8)
# print(f"answer = {operation_calc}")
def calculation():
    calculation_continue = True
    # Program asks the user to type the first number.
    num1 = float(input("Enter the first number?: "))

    while calculation_continue:
    # Program asks the user to type a mathematical operator (a choice of "+", "-", "*" or "/")
        for symbols in operation:
            print(symbols)
        operation_symbols = input("Pick an operation: ")
        # Program asks the user to type the second number.
        num2 = float(input("What's the next number?: "))
        # Program works out the result based on the chosen mathematical operator.
        answer = operation[operation_symbols](num1, num2)
        print(f"{num1} {operation_symbols} {num2} = {answer}")
        # Program asks if the user wants to continue working with the previous result.
        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
        # If yes, program loops to use the previous result as the first number and then repeats the calculation process.
        if choice == "y":
            num1 = answer
        # If no, program asks the user for the fist number again and wipes all memory of previous calculations.    
        else:
            calculation_continue = False
            print("\n" * 10)
            calculation()
        # Add the logo from art.py
calculation()

