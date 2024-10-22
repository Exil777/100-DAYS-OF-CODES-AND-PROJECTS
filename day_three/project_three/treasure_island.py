# Treasure Island game
# the mission is to find the treasure
# User is ask to pick some options and each options get the user closer to wining the treasure 

# the first question ask the user to pick which direction the wants to go: Left or right? and base on the user answer the user can keep going to the next question or loose the game 

# the next question is: if the user want to swim or wait, just like the first question, if the user pick the wrong answer, the user loose the game

# the next question is: which door color the user wants to pick

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# asking the user to pick pick between left of right
first_choice = input('You\'re at a cross road. Where do you want to go?\n\tType "left" or "right"\n').lower()

if first_choice == "left":
    # if the user pick left, the user is ask to pick between wait or wwim
    second_choice = input('You\'ve come to a lake. There is an island in the middle of the lake.\nType "wait" to wait for a boat. Tpe "swim" to swim across.\n').lower()

    if second_choice == "wait":
        # if the user pick wait, the user is ask to pick between different doors color
        third_choice = input("You arrive at the island unharmed. There is a house with 3 doors.\nOne red, one yellow and one blue. Which color do you choose?\n") .lower()

        if third_choice == "yellow":
            # if the user pick yellow he found the treasure
            print("Congradulation, You find the treasure")
        else:
            # if he pick any other option, the program let the user know that he lost the game
            print("Sorry, no treasure")
    else:
        # if the user decide to swim instead of wait, the program let the user know that he lost the game
        print("You lost, be patient and wait next time")
else:
    # if the user decide to go right instead of left, the program let the user know that he lost the game
    print("You lost, better luck next time")

        