#!/usr/bin/python3

from art import logo


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


function_execution = True


def encrypt(text, shift):
    encrypted_letters = []
    for l in text:
        if l in alphabet:
            x = alphabet.index(l)
            encypted_value = x + shift
            # print(f"encypted_value: {encypted_value}")
            while encypted_value > 25:
                encypted_value = encypted_value - 26
            encrypted_letters.append(alphabet[encypted_value])
        else:
            encrypted_letters.append(l)
    encrypted_str = ''.join(encrypted_letters)
    print(f'Your Encypted text is "{encrypted_str}"')
    return encrypted_str


def decode(text, shift):
    encrypted_letters = []
    for l in text:
        if l in alphabet:
            x = alphabet.index(l)
            encypted_value = x - shift
            # print(f"encypted_value: {encypted_value}")
            while encypted_value < 0:
                encypted_value = encypted_value + 26
            encrypted_letters.append(alphabet[encypted_value])
        else:
          encrypted_letters.append(l)
    encrypted_str = ''.join(encrypted_letters)
    print(f'Your decoded text is "{encrypted_str}"')

def get_encryption_type():
    get_input = True
    while get_input:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction == 'encode' or direction == 'decode':
            get_input = False
    return direction


def run_again():
    get_input = True
    while get_input:
        again = input("\nWould you like to encode or decode something else, y or n? \n").lower()
        if again == 'y' or again == 'n':
            get_input = False
    if again == "n":
        function_execution = False
        print("Good Bye")
    else:
        function_execution = True
    return function_execution


def caesar():
    print(logo)
    encryption_type = get_encryption_type()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if encryption_type == "encode":
        encrypt(text, shift)
    elif encryption_type == "decode":
        decode(text, shift)
    # cipher_text = encrypt(text, shift)
    # decode(cipher_text, shift)


while function_execution:
  caesar()
  function_execution = run_again()

