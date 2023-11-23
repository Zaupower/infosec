import base64
import codecs
from Crypto.Cipher import AES
from Crypto.Hash import SHA256


def validate_aes_key(key):
    key_size = len(key.encode()) * 8  # Convert bytes to bits
    print(f'Key size: {key_size}' )
    return key_size in [128, 192, 256]

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def rot13(text):
    return codecs.encode(text, 'rot_13')

def aes_encrypt(text, key):
    cipher = AES.new(key.encode(), AES.MODE_ECB)
    padded_text = text + ' ' * ((16 - len(text) % 16) % 16)
    encrypted_text = cipher.encrypt(padded_text.encode())
    return base64.b64encode(encrypted_text).decode()

def aes_decrypt(encrypted_text, key):
    cipher = AES.new(key.encode(), AES.MODE_ECB)
    decrypted_text = cipher.decrypt(base64.b64decode(encrypted_text)).decode().rstrip()
    return decrypted_text

def sha256_hash(text):
    hash_object = SHA256.new(data=text.encode())
    return hash_object.hexdigest()

def main():
    while True:
        print("\nChoose a cryptographic method:")
        print("a. Caesar's Cipher")
        print("b. ROT13")
        print("c. AES")
        print("d. SHA256 (hashing algorithm, non-reversive)")
        print("e. Exit")

        choice = input("Enter your choice: ")

        if choice.lower() == 'e':
            break

        operation = input("Do you want to encrypt or decrypt? (e/d): ")
        message = input("Enter the message: ")

        if choice.lower() in ('a', 'b', 'c'):
            key = input("Enter the key: ")

        if choice.lower() == 'a':
            shift = int(key)
            if operation.lower() == 'e':
                result = caesar_cipher(message, shift)
            elif operation.lower() == 'd':
                result = caesar_cipher(message, -shift)
            else:
                print("Invalid operation. Please enter 'e' for encrypt or 'd' for decrypt.")
                continue

        elif choice.lower() == 'b':
            if operation.lower() == 'e':
                result = rot13(message)
            elif operation.lower() == 'd':
                result = rot13(message)
            else:
                print("Invalid operation. Please enter 'e' for encrypt or 'd' for decrypt.")
                continue

        # elif choice.lower() == 'c':
        #     if operation.lower() == 'e':
        #         result = aes_encrypt(message, key)
        #     elif operation.lower() == 'd':
        #         result = aes_decrypt(message, key)
        #     else:
        #         print("Invalid operation. Please enter 'e' for encrypt or 'd' for decrypt.")
        #         continue

        elif choice.lower() == 'c':
            if not validate_aes_key(key):
                valid = False
                while not valid:
                    key = input("Enter the key: ")
                    valid = validate_aes_key(key)
                    print(f'VALID: {valid}')
            if operation.lower() == 'e':
                result = aes_encrypt(message, key)
            elif operation.lower() == 'd':
                result = aes_decrypt(message, key)
            else:
                print("Invalid operation. Please enter 'e' for encrypt or 'd' for decrypt.")
                continue        

        elif choice.lower() == 'd':
            print("SHA256 is a hashing algorithm. It cannot be decrypted.")
            result = sha256_hash(message)

        else:
            print("Invalid choice. Please enter a valid option.")

        print(f"Result: {result}")

if __name__ == "__main__":
    main()