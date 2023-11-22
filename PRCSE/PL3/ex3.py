'''
Write a script that receives a word as argument and verifies if it is a palindrome. A palindrome
is a sequence of characters which reads the same backward as forward, such as madam or
racecar.
'''

word = str(input('Write a word to check if it is palindrome\n'))

is_palindrome = word == word[::-1]
if is_palindrome:
    print('Is palindrome')
else:
    print('Is not palindrome')

