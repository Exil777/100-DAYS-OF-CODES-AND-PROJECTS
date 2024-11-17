# Functiion with output
def format_name(f_name, l_name):
    first_name = f_name.title()
    last_name = l_name.title()
    return f"{first_name} {last_name}"

formatd_string = format_name(f_name="jameson", l_name="exil")
print(formatd_string)