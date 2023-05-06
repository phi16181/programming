import random
word = ['g','a','m','e']
hint = []
rand_choice = random.choice(word)
print(rand_choice)
turn_ind = word.index(rand_choice)
print(turn_ind)

for letter in word:
    hint.append('_')

print(hint)
#display.insert(turn_ind,rand_choice)
#when guess is in the word
hint[turn_ind] = rand_choice
print(f'Excellent guess! Here is the updated hint: {hint}')




