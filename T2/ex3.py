import sys
from stegano import lsb
from PIL import Image


def decode_lsb(image_path):
    clear_message = lsb.reveal(image_path)
    return clear_message

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def bruteforce_ceaser(text, number_of_tries):
    for i in range(number_of_tries):
        print(str(i) + " "+ caesar_cipher(text, i))

# Decode message from encoded image

# Check command number of command line arguments
if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <path>")
else:
    decoded_message = decode_lsb(sys.argv[1])
    if decoded_message:
        print("Message found: " + decoded_message)
        tries = int(input(f"Please input the number of tries to bruteforce with ceaser cypher, maximum possible number of tries 26\n"))
        bruteforce_ceaser(decoded_message, tries)
    else:
        print("No message found in image")




