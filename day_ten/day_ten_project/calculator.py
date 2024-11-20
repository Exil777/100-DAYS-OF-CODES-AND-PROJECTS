# TODO: Write out the other 3 functions - subtract, multiply and divide.
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2 

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    n1 / n2
# TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"
operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
# TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.
operation_calc = operation["*"](4, 8)
print(f"answer = {operation_calc}")



# Program asks the user to type the first number.
# Program asks the user to type a mathematical operator (a choice of "+", "-", "*" or "/")
# Program asks the user to type the second number.
# Program works out the result based on the chosen mathematical operator.
# Program asks if the user wants to continue working with the previous result.
# If yes, program loops to use the previous result as the first number and then repeats the calculation process.
# If no, program asks the user for the fist number again and wipes all memory of previous calculations.
# Add the logo from art.py

# num1 = input("Enter the first number?: ")