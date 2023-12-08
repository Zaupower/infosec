from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os

def aes_file_operation(file_path, key, mode='encrypt'):
    if mode not in ['encrypt', 'decrypt']:
        raise ValueError("Invalid mode. Use 'encrypt' or 'decrypt'.")

    # Read the content of the file
    with open(file_path, 'rb') as file:
        data = file.read()

    # Generate a random IV (Initialization Vector)
    iv = os.urandom(16)

    # Create an AES cipher object
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())

    if mode == 'encrypt':
        # Pad the data to be a multiple of 16 bytes (block size)
        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        padded_data = padder.update(data) + padder.finalize()

        # Encrypt the padded data
        encryptor = cipher.encryptor()
        result = encryptor.update(padded_data) + encryptor.finalize()

        # Write the IV and ciphertext to the output file
        output_file_path = file_path + ".enc"
        with open(output_file_path, 'wb') as output_file:
            output_file.write(iv + result)

        print(f"File encrypted and saved as {output_file_path}")

    elif mode == 'decrypt':
        # Separate IV and ciphertext
        received_iv = data[:16]
        ciphertext = data[16:]

        # Decrypt the ciphertext
        decryptor = cipher.decryptor()
        decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()

        # Unpad the decrypted data
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        result = unpadder.update(decrypted_data) + unpadder.finalize()

        # Write the result to the output file
        output_file_path = file_path + ".dec"
        with open(output_file_path, 'wb') as output_file:
            output_file.write(result)

        print(f"File decrypted and saved as {output_file_path}")

def decrypt_files_in_folder(folder_path, key):
    for root, _, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith(".enc"):
                file_path = os.path.join(root, filename)
                aes_file_operation(file_path, key, mode='decrypt')

# Example usage
folder_path = 'path/to/your/folder'
key = b'sixteen_byte_key'  # 128-bit key

# Decrypt all files in the folder and its subfolders
decrypt_files_in_folder(folder_path, key)

