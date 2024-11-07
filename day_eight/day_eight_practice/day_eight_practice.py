# Function and parameters
def greet():
    print("Hello World")
    print("My name is Jameson")

greet()
# declaring a function call 'great()' and calling the function

def greet_with_name(first_name, last_name):
    print(f"Hello my name is {first_name} {last_name}")
greet_with_name("Jameson", "Exil")
# declaring a function call 'greet_with_name' with two parameters and passing two arguments when calling the function

#Create a function called life_in_weeks() using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.
def life_in_weeks(current_age):

    total_years = 90
    weeks_in_year = 52
    
    weeks_in_total_year = total_years * weeks_in_year
    weeks_in_current_age = current_age * weeks_in_year 

    years_left = weeks_in_total_year - weeks_in_current_age
    print(f"You have {years_left} weeks left.")

life_in_weeks(56)


def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")
greet_with(name="Jameson", location="Dallas")
# declaring 'greet_with' function with two parameter and two keyword arguments



#You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people: 

#1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   

#2. Then check for the number of times the letters in the word LOVE occurs.   

#3. Then combine these numbers to make a 2 digit number and print it out. 
def calculate_love_score(name1, name2):
    names_combine = name1 + name2
    lower_names = names_combine.lower()

    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_compatibility = t + r + u + e 

    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    sencond_compatibility = l + o + v + e 

    total_number_compatibility = int(str(first_compatibility) + str(sencond_compatibility))
    print(total_number_compatibility)

calculate_love_score("Jameson", "Exil")