import random
word_list = ['apple', 'knife', 'soccer', 'computer']

# TODO-1 Randomly choose a word from the word_list and assign it to a variable called chosen_word, the print it
chosen_word = random.choice(word_list)
print(chosen_word)
# TODO-4 Create a "placeholder" with the same number of blanks as the chosen_word
placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"
print(placeholder)
# TODO-2 Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lower case
guess = input("Guess a letter: ").lower()
# TODO-3 check if the letter the user guessed (guess) is one of the letters in the chosen_word. print "Right" if it is, "Wrong" if it's not
# TODO-5 Create a "display" that puts the guess letter in the right position and _ in the rest of the string.
display = ""

for letter in chosen_word:
    if letter == guess:
        #print("Right")
        display += letter
    else:
        #print("Wrong")
        display += "_"

print(display)