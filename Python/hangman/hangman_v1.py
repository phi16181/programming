#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   hangman_v1.py
@Time    :   2023/05/06 13:17:52
@Author  :   Benjamin Manning 
@Version :   3.0
@Contact :   benjaminbmanning@gmail.com
@License :   (C)Copyright 2023-2024, Benjamin Manning
@Desc    :   None
'''


#import needed libraries
import random as rd
import os
#'the word' of the day
base_word = rd.choice(['one', 'two', 'three'])
#split into components for counting
the_word = []
for x_letter in base_word:
    the_word.append(x_letter)
num_of_letters = len(the_word)
#empty for holding letter choices
chosen_letters = []
turns = 6
#user chooses a letter

while turns != 0 or num_of_letters == 0:
    print(the_word)
    letter = input('Please choose a letter: ')
    if not letter.isalpha():
        print('You did not enter a letter; please redo this')
    # letter is chosen, has not been used, and is not in the word
    elif letter not in chosen_letters and letter not in the_word: #this works
        #actions: -+ 1 a turn, add letter to 'chosen already', notify player
        turns -= 1
        print('You guess incorrectly; you lose a turn, sucka!')
        chosen_letters.append(letter)
        #debugging
        print(f'letters chosen so far: {chosen_letters}')
        print(f'Number of letters left in the word: {num_of_letters}')
        #letter is chosen, has already been used
    elif letter in chosen_letters: #this works
        #actions: -= 1 a turn, notify player
        print('That letter has already been used, sucka! You lose a turn, now choose again')
        turns -= 1
        #debugging
        print(f'letters chosen so far: {chosen_letters}')
        print(f'Number of letters left in the word: {num_of_letters}')
    #letter is chosen and is in the word
    elif letter not in chosen_letters and letter in the_word: #this works
        #actions: add letter to 'chosen already', update letter in word list, notify player
        chosen_letters.append(letter)
        num_of_letters -= 1
        print(f'{letter} is in the word!; make another choice')
        print(f'letters chosen so far: {chosen_letters}')
        print(f'Number of letters left in the word: {num_of_letters}')
        #user wins
    if num_of_letters == 0:
        print(f'you won! The word is {base_word}')
        break
    #out of turns
    if turns == 0:
        print('Game Over')
        break










