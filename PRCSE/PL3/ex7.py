'''
Password Validator with Python
a. Read a password as input.
b. Verify if the password has between 8-16 characters.
c. Consider a valid password if it contains lower case characters, upper case characters,
numbers, and symbols.
'''

def password_check(passwd):
     
    SpecialSym =['$', '@', '#', '%']
    val = True
     
    if len(passwd) < 8 or len(passwd) > 16:
        print('length should be between 8 and 16')
        val = False
        
    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one numeral')
        val = False
         
    if not any(char.isupper() for char in passwd):
        print('Password should have at least one uppercase letter')
        val = False
         
    if not any(char.islower() for char in passwd):
        print('Password should have at least one lowercase letter')
        val = False
         
    if not any(char in SpecialSym for char in passwd):
        print('Password should have at least one of the symbols $@#')
        val = False
    if val:
        return True
    

#password = str(input('Test a password\n'))
#password_check(password)