'''
Write a python program that, when provided with an image’s path and a message, performs
Least Significant Bit (LSB) Steganography. The program should also provide an option to
extract a hidden message from an image through LSB.
'''
from stegano import lsb
from PIL import Image

def encode_lsb(image_path, message, output_path):
    secret = lsb.hide(image_path, message)
    secret.save(output_path)

def decode_lsb(image_path):
    clear_message = lsb.reveal(image_path)
    return clear_message

# Example usage
image_path = "'./supportfiles/ips.txt'"
message_to_hide = "Hello, this is a hidden message!"
output_image_path = "path/to/your/output/ips_encoded.png"

# Encode message into image
encode_lsb(image_path, message_to_hide, output_image_path)

# Decode message from encoded image
decoded_message = decode_lsb(output_image_path)
print("Decoded Message:", decoded_message)