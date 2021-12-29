"""
File: anagram.py
Name: 陳名娟 Jenny Chen
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# global variable
dictionary = []


def main():
    """
    To find the anagrams of the word inputted by user.
    """
    start = time.time()
    ####################
    print(f'Welcome to stanCode \"Anagram Generator\" (or {EXIT} to quit)')
    read_dictionary()
    while True:
        word = input('Find anagram for: ')
        if word == EXIT:
            break
        else:
            find_anagrams(word)
    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    with open(FILE, 'r') as f:
        for line in f:
            dictionary.append(line.strip())


def find_anagrams(s):
    """
    :param s: str, the main word inputted by user to find anagrams
    """
    count = [0]
    ans_list = []
    find_anagrams_helper(s, '', ans_list, count, [])
    print('Searching...')
    print(str(count[0]) + ' anagrams: ' + str(ans_list))


def find_anagrams_helper(s, current_str, ans_list, count, index_list):
    """
    :param s: str, to find anagrams of the main word inputted by user
    :param current_str: str,
    :param ans_list: list, include the anagrams
    :param count: list, the index 0 is the number of the anagrams
    :param index_list: list, the index list
    """
    if len(current_str) == len(s):
        if current_str in dictionary:
            if current_str not in ans_list:
                ans_list.append(current_str)
                count[0] += 1
                print('Searching...')
                print(f'Find: {current_str}')
    else:
        for i in range(len(s)):
            alpha = s[i]
            if i not in index_list:     # 使用index以確保每個字母都有列入考慮
                # choose
                index_list.append(i)
                current_str += alpha

                # explore
                if has_prefix(current_str):    # 當有該字開頭之字首, 才繼續explore
                    find_anagrams_helper(s, current_str, ans_list, count, index_list)

                # un-choose
                index_list.pop()
                current_str = current_str[0:len(current_str)-1]


def has_prefix(sub_s):
    """
    :param sub_s: str, the part of the word
    :return: the boolean answer
    """
    for word in dictionary:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
