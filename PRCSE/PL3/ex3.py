'''
Write a script that receives a word as argument and verifies if it is a palindrome. A palindrome
is a sequence of characters which reads the same backward as forward, such as madam or
racecar.
'''

word = str(input('Write a word to check if it is palindrome\n'))

is_palindrome = word == word[::-1]
word_len = len(word)
if word_len < 2:
    print('Is palindrome')
else:
    word_half_size = int(word_len/2)
    is_palidrome = True
    for i in range(word_half_size):
        if word[i] != word[word_half_size+i]:
            is_palidrome = False
            break
    print(f'Is palindrome: {is_palidrome}')

