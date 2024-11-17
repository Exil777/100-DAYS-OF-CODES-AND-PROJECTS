# Functiion with output
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did not provide a valid inputs"
    first_name = f_name.title()
    last_name = l_name.title()
    return f"{first_name} {last_name}"

formatd_string = format_name(input("What is your first name? "), input("What is your last name? "))
print(formatd_string)