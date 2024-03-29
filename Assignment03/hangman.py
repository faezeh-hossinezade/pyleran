from random import randint

words = ['housekeeping', 'cracking', 'call off something', 'deputy', 'appreciate', 'trail', 'spicy', 'tease']

index = randint(0, len(words) - 1)
word = words[index]
i = 1

true_char = []
false_char = []

while i < 7:
    win = True
    for char in word:
        if char == ' ':
            print(' / ', end='')
        elif char in true_char:
            print(f'{char} ', end='')
        else:
            print('_ ', end='')
            win = False
    if win:
        print('\nYou Win Babe')
        break
    
    user_char = input(f'Please Enter Char ({i}): ').lower()

    if len(user_char) != 1:
        print('\none to one please!!!')
    elif user_char in word:
        true_char.append(user_char)
    else:
        false_char.append(user_char)
        i += 1

if i >= 7:
    print('\nYou Lose Babe')
    print('The Correct word was', word)