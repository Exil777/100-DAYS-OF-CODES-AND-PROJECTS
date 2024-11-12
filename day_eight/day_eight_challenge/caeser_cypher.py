from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, decode_or_encode):

    output_text = ""
    if decode_or_encode == "decode":
            shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
             output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]

    print(f"Here is the {decode_or_encode}d result: {output_text}")


game_continue = True
while game_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, decode_or_encode=direction)

    resart = input("Type 'yes' if you want to continue. Otherwise type 'no'\n").lower()
    if resart == "no":
         game_continue = False
         print("Thank you for playing. Good bye.")


# TODO-1: Import and print the logo from art.py when the program starts.
# TODO-2: What happens if the user enters a number/symbol/space?
# TODO-3: Can you figure out a way to restart the cipher program?




# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
# def encrupt(original_text, shift_amount):
# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.
    # cipher_text = ""
    # for letter in original_text:
    #     shifted_position = alphabet.index(letter) + shift_amount

    #     shifted_position %= len(alphabet) 
    #     cipher_text += alphabet[shifted_position]
    # print(f"Encoded result {cipher_text}")
# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.
# encrupt(original_text=text, shift_amount=shift)

# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.

# def decrypt(original_text, shift_amount):
#     output_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) - shift_amount

#         shifted_position %= len(alphabet)
#         output_text += alphabet[shifted_position]

#     print(f"Decoded result {output_text}")

# decrypt(original_text=text, shift_amount=shift)
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.
