
from stegano import lsb
from PIL import Image


def decode_lsb(image_path):
    clear_message = lsb.reveal(image_path)
    return clear_message

# Example usage
output_image_path = "PRCSE-C2.png"

# Decode message from encoded image
decoded_message = decode_lsb(output_image_path)
print("Decoded Message:", decoded_message)
