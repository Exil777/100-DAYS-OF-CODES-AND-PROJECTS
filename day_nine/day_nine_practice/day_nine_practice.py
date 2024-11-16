programing_dictionary = {
    "Bug":"An error in a program that prevents the program from running as expected.",
    "Function":"A piece of code that you can easily call over and over again.",
}

# retreiving an item from the dict
# print(programing_dictionary["Bug"])

# adding an item into our dict
programing_dictionary["Loop"] = "The action of doing something over and over again"

# print(programing_dictionary)

# looping through a dictionary
for key in programing_dictionary:
    print(key)
    print(programing_dictionary[key])



# dictionary
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nested List in Dict
# travel_log = {
#     "France": ["Paris", "Lille", "Dihon"],
#     "Germany": ["stuttgart", "Berlin"],
# }

# print(travel_log["France"][1])

# Nested list
nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])

# Nested Dict in Dict
travel_log = {
    "France": {
        "total_visits": 12,
        "cities_visited": ["Paris", "lille", "Dijon"]
    },
    "Germany": {
        "total_visits": 8,
        "cities_visited": ["stuttgart", "Berlin"],
    }
}

print(travel_log["France"]["total_visits"])
print(travel_log["Germany"]["cities_visited"][1])