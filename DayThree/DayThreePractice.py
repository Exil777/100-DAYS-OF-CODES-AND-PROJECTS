# Check to see if a number input from the user is odd or even

number_to_check = int(input("Enter a number you want to check: "))

if number_to_check % 2 == 0:
    print(f"number {number_to_check} is an even number")
else:
    print(f"number {number_to_check} is an odd number")