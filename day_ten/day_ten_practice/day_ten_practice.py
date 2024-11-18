# Functiion with output
def format_name(f_name, l_name):
    """Take a first and last name and format it to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "You did not provide a valid inputs"
    first_name = f_name.title()
    last_name = l_name.title()
    return f"{first_name} {last_name}"

formatd_string = format_name(input("What is your first name? "), input("What is your last name? "))
print(formatd_string)


# Write a program that returns True or False whether if a given year is a leap year.

# This is how you work out whether if a particular year is a leap year. 

# - on every year that is divisible by 4 with no remainder

# - except every year that is evenly divisible by 100 with no remainder 

# - unless the year is also divisible by 400 with no remainder   


def is_leap_year(year):
    # Write your code here. 
    """Take year and check to see if it's a leap year or not."""
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
    # Don't change the function name.
print(is_leap_year(2400))