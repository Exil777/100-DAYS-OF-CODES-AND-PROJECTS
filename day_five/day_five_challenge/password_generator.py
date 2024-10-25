# The objective is to take the inputs from the user to these questions and then generate a random password. Use your knowledge about Python lists and loops to complete the challenge.

import random
# list of letters
letters = ['a','b','c','d','e','f','g','h','e','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# list of numbers
numbers = ['0','1','2','3','4','5','6','7','8','9']
# list of symbols
symbols = ['!','#','$','%','&','(',')','*','+']



print('Welcome to the Password Generator')
# asking the user for the number of letters the user would like to enter for the password
nr_letters = int(input('How many letters would you like in your password?\n'))
# asking the user for the number of symbols the user would like to enter for the password
nr_symbols = int(input('How many symbols would you like?\n'))
# asking the user for the number of numbers the user would like to enter for the password
nr_numbers = int(input('How many numbers would you like?\n'))

# create an empty list so user random password can be added too
password_list = []

# looping through the range of number from 0 to the number of letter the user chooses 
# so we can determing how many letters the password needs
for char in range(0, nr_letters):
    # adding the ranges numbers of letters at random from the letters list at random to the password_list list variable
    password_list += random.choice(letters)

for number in range(0, nr_numbers):
    password_list += random.choice(numbers)

for symbol in range(0, nr_symbols):
    password_list += random.choice(symbols)

# shuffling the values inside the passward_list list
random.shuffle(password_list)

# converting the password_list list into a string value

password = ''

# looping to each individual list value and assign each value to char
for char in password_list:
    # adding or append each value to the empty string variable password
    password += char
print(password)



