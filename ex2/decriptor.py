import os
from pathlib import Path
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES


privateKeyFile = '/home/marcelo/Documents/infosec/ex2/private.pem'


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


def decrypt(dataFile, privateKeyFile):
    '''
    use EAX mode to allow detection of unauthorized modifications
    '''
    # read private key from file
    extension = dataFile.suffix.lower()
    with open(privateKeyFile, 'rb') as f:
        privateKey = f.read()
        # create private key object
        key = RSA.import_key(privateKey)

    # read data from file
    with open(dataFile, 'rb') as f:
        # read the session key
        encryptedSessionKey, nonce, tag, ciphertext = [ f.read(x) for x in (key.size_in_bytes(), 16, 16, -1) ]

    # decrypt the session key
    cipher = PKCS1_OAEP.new(key)
    print(str(encryptedSessionKey))
    sessionKey = cipher.decrypt(encryptedSessionKey)

    # decrypt the data with the session key
    cipher = AES.new(sessionKey, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)

    # save the decrypted data to file
    dataFile = str(dataFile)
    fileName= dataFile.split(extension)[0]
    fileExtension = '.decrypted' # mark the file was decrypted
    decryptedFile = fileName + fileExtension
    with open(decryptedFile, 'wb') as f:
        f.write(data)

    print('Decrypted file saved to ' + decryptedFile)


#directory = str(input('Directory to decript:\n'))
directory = "/home/marcelo/Documents/infosec/ex2/TestRamsware"
if directory:
    excludeExtension = ['.py','.pem', '.exe'] 
    for item in scanRecurse(directory): 
        filePath = Path(item)
        fileType = filePath.suffix.lower()

        if fileType in excludeExtension:
            continue
        print(Path(filePath))
        decrypt(filePath, privateKeyFile)