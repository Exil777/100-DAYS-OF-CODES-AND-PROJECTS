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