import random
word_list = ['apple', 'knife', 'soccer', 'computer']

# TODO-1 Randomly choose a word from the word_list and assign it to a variable called chosen_word, the print it
chosen_word = random.choice(word_list)
print(chosen_word)
# TODO-2 Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lower case
guess = input("Guess a letter: ").lower()
# TODO-3 check if the letter the user guessed (guess) is one of the letters in the chosen_word. print "Right" if it is, "Wrong" if it's not
for letter in chosen_word:
    if letter == chosen_word:
        print("Right")
    else:
        print("Wrong")