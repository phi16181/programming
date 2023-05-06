#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   hangman_v2.py
@Time    :   2023/05/06 13:17:52
@Author  :   Benjamin Manning 
@Version :   3.0
@Contact :   benjaminbmanning@gmail.com
@License :   (C)Copyright 2023-2024, Benjamin Manning
@Desc    :   None

Whats new in V2?
Added functionality:
1. placeholder display for chosen letters included in the word
2. 'lost turn' counter in the form of 'YOULOSE' list (rather than displaying a hanged illustration
3. Refactor of earlier code into functions, where applicable
"""

#import needed libraries
import random as rd
import os
#'the word' of the day
base_word = rd.choice(['one', 'two', 'three'])
#unpack for counting,indexing, etc.
base_word = ([*base_word])

#number of turns
turns_word = rd.choice(['YOU LOSE', 'GAME OVER', 'LIGHTS OUT'])
turns_word_unpack = ([*turns_word])
turns = -1

#empties for holding values
chosen_letters = []
hint_board_letters = []
individual_letters = []
turns_display = []

#hint board and counter lists
for letter in base_word:
    individual_letters.append('_')
    hint_board_letters.append('_')

for letter in turns_word_unpack:    
    turns_display.append('_')

#count the number of letters in the process, when this hits 0, the user wins
num_of_letters = len(individual_letters)

while num_of_letters != 0:
    print(f'Here are your hints: {hint_board_letters}')
    print('-----------------')
    letter = input('Please choose a letter: ')
    if not letter.isalpha():
        print('You did not enter a letter; please redo this')
    # letter is chosen and is in the base word - first choice
    elif letter in base_word:
        #actions: add letter to 'chosen already', update letter in word list, notify player
        chosen_letters.append(letter)
        turn_index = base_word.index(letter)
        hint_board_letters[turn_index] = letter
        #upadte letter in word list
        num_of_letters -= 1
        #notify player
        print(f'Excellent guess! Here is the updated hint: {hint_board_letters}')
        print('----------------')
        print(f'letters chosen so far: {chosen_letters}')
        print(f'Turns: {turns_display}')
        #print(f'Number of letters left in the word: {num_of_letters}')
    elif letter not in chosen_letters and letter not in base_word: 
        #actions: -+ 1 a turn, add letter to 'chosen already', notify player
        print('You guess incorrectly; you lose a turn, sucka!')
        print('----------------')
        chosen_letters.append(letter)
        turns += 1
        turns_update = turns_word_unpack[turns]
        turns_display[turns] = turns_update
        print(turns_display)
        #debugging
        #print(f'letters chosen so far: {chosen_letters}')
        #print(f'Number of letters left in the word: {num_of_letters}')    
    #letter is chosen, has already been used
    elif letter in chosen_letters: #this works
        #actions: -= 1 a turn, notify player
        print('That letter has already been used, sucka! You lose a turn, now choose again')
        turns += 1
        #debugging
        #print(f'letters chosen so far: {chosen_letters}')
        #print(f'Number of letters left in the word: {num_of_letters}')
    #user wins
    if num_of_letters == 0:
        print(f'you won! The word is {base_word}')
        break
    #out of turns - user loses
    if turns == len(turns_word_unpack):
        print('Game Over')
        break










