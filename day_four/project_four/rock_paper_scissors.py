# Rock, paper, and scissor game 
# user will have the option to choose between 0, 1, 2
# 0 will be assign to rock, 1 will be assign to paper, and 2 will be assign to scissors
# base on the user choice the program will pick an option at random and base on that choice, the user or the computer will be the winner

import random

rock_paper_scissors = ["rock", "paper", "scissors"]

user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n"))
print(f"{rock_paper_scissors[user_choice]}\n")

computer_choice = random.randint(0, 2)
print(f"Computer chose:\n{rock_paper_scissors[computer_choice]}")

if user_choice >= 3 or user_choice < 0:
    print("Enter a valid number")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 2 and computer_choice == 0:
    print("You lost!")
elif computer_choice > user_choice:
    print("Computer win!")
elif user_choice > computer_choice:
    print("You win!")
elif user_choice == computer_choice:
    print("It's a draw!")






