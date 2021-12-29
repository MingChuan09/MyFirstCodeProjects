"""
File: hangman.py
Name: 陳名娟 Jenny Chen
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    turn = N_TURNS          # the left times the player has
    secret = random_word()  # the answer of the game
    ans = ''                # make the answer unknown
    for ch in secret:
        ans += '-'
    print('The word looks like: '+str(ans))        # let player knows the length of the answer
    print('You have '+str(turn)+' guesses left.')  # let player knows the left times they has
    ans1 = ans
    while True:
        guess = input('Your guess: ')    # get word the player guessed
        guess = guess.upper()            # case-sensitive
        if not guess.isalpha():          # confirm if guess is alpha
            print('Illegal format.')
        elif len(guess) != 1:            # confirm if guess is only one word
            print('Illegal format.')
        elif secret.find(guess) == -1:   # if the answer isn't include guess
            turn -= 1                    # the left times will minus 1
            print('There is no ' + str(guess) + '\'s in the word.')
            if turn > 0:
                print('The word looks like: ' + str(ans1))
                print('You have ' + str(turn) + ' guesses left.')
            else:
                print('You are completely hung :(')    # there is no times for player
                break
        else:
            turn = turn                             # the left times player having will not change
            ans1 = replace(secret, ans1, guess)
            print('You are correct!')
            if ans1 != secret:                      # the answer having some unknown word
                print('The word looks like: ' + str(ans1))
                print('You have ' + str(turn) + ' guesses left.')
            else:                                   # the player gets the answer
                print('You win!!')
                break
    print('The word was: '+str(secret))


def replace(original, old_word, new_word):
    """
    If new_word is in original, this function will
    replace old_word with new_word.
    """
    ans = ''
    for i in range(len(original)):
        if new_word == original[i]:
            ans += new_word
        else:
            ans += old_word[i]
    return ans


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
