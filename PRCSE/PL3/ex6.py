'''
Guessing Game with Python
    a. Generate a random number at the beginning of the game.
    b. Tell the user if the number he guessed is lower, higher, or equal to the generated number
    (stop the game when he is right).
    c. Track the total number of user guesses and display this information at the end of the
    game.
    d. Ask if the user wants to play again (or leave) and, if so, re-start the game.
'''
import random
rn = random.randint(0,9)
game_again = True


def test_num():
    guess_number = int(input('Guess the number\n'))
    if guess_number > rn : 
        return 1
    elif guess_number < rn :
        
        return -1
    else: 
        return 0
    
def switch(res):
    if res == 0:
        print('You got it!!')
        exit
    elif res == -1:
        print('Guess higher!!')
    elif res == 1:
        print('Guess lower!!')
    
    game_again = str(input('Do you want to play again(y/n)?\n'))

    if game_again == "y":
        return True
    elif game_again == "n":
        return False


def game():
    while True:
        res = test_num()
        if not switch(res):
            break
game()