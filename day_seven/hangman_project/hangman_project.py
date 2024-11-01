import random
# TODO-9: - Update the word list to use the 'word_list' from hangman_words.py
from hangman_words import word_list
from hangman_art import stages, logo

# TODO-8 Create a variable called "Lives" to keep track of lives left
lives = 6
print(logo)
#word_list = ['apple', 'knife', 'soccer', 'computer']

# TODO-1 Randomly choose a word from the word_list and assign it to a variable called chosen_word, the print it
chosen_word = random.choice(word_list)
print(chosen_word)
# TODO-4 Create a "placeholder" with the same number of blanks as the chosen_word
placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"
print(placeholder)

# TODO-6 Use a while loop to let the user guess again
game_over = False
correct_letters = []
# TODO-2 Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lower case
while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")

    guess = input("Guess a letter: ").lower()

# TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in correct_letters:
        print(f"You've already guessed {guess}")

# TODO-3 check if the letter the user guessed (guess) is one of the letters in the chosen_word. print "Right" if it is, "Wrong" if it's not
# TODO-5 Create a "display" that puts the guess letter in the right position and _ in the rest of the string.
    display = ""
#TODO-7 Change the for loop so that you keep the previous correct letters in the diplay
    for letter in chosen_word:
        if letter == guess:
            #print("Right")
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            #print("Wrong")
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        print(f"You have {lives} left")
        if lives == 0:
            game_over = True
            print(f"***********************It was {chosen_word}! YOU LOSE**********************")


    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])

    