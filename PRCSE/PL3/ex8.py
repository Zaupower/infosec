'''
Password Generator with Python
a. When requested generate a random password with python.
b. The password must be valid according to your python password validator (exercise 7).
'''
import string
import random
from ex7 import password_check
 
# Getting password length
length = random.randint(8, 16)
characterList = ['$', '@', '#', '%']
 
# Getting character set for password
characterList += string.digits
characterList += string.ascii_uppercase
characterList += string.ascii_lowercase
 

def gen_password():
    password = []
    for i in range(length):
        randomchar = random.choice(characterList)
        password.append(randomchar)

    return password    
    

password = "".join(gen_password())

while not password_check(password):
    password = "".join(gen_password())
# printing password as a string
print("The random password is " + "".join(password))