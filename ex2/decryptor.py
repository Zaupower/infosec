import os
from pathlib import Path
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES


privateKeyFile = 'private.pem'


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
            
def decrypt(dataFile, privateKeyFile, extension):
    #use EAX mode to allow detection of unauthorized modifications
    # read private key from file
    extension = dataFile.suffix.lower()
    with open(privateKeyFile, 'rb') as f:
        privateKey = f.read()
        # create private key object
        key = RSA.import_key(privateKey)

    # read data from file
    with open(dataFile, 'rb') as f:
        # Read the session key
        key_size = key.size_in_bytes()
        encryptedSessionKey = f.read(key_size)
        nonce = f.read(16)
        tag = f.read(16)
        ciphertext = f.read()

    # decrypt the session key
    cipher = PKCS1_OAEP.new(key)
    sessionKey = cipher.decrypt(encryptedSessionKey)

    # decrypt the data with the session key
    cipher = AES.new(sessionKey, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)

    # save the decrypted data to file
    dataFile = str(dataFile)
    fileName= dataFile.split(extension)[0]
    decryptedFile = fileName + "-DECRIPTED-" + extension
    with open(decryptedFile, 'wb') as f:
        f.write(data)
    print('Decrypted file saved to ' + decryptedFile)
#directory = '/home/' #real dir
directory = '/home/marcelo/Documents/infosec/ex2/TestRansomware/'

dir = input('put your directory (default is "TestRamsware" ):')
if dir:
  directory = dir
for item in scanRecurse(directory): 
    filePath = Path(item)
    fileType = filePath.suffix.lower()
    decrypt(filePath, privateKeyFile, fileType)