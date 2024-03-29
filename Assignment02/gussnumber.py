import random

i = 0
computer_number = random.randint(0, 100)

while True:
    user_number = int(input())
    i += 1

    if user_number < computer_number:
        print('Go Up 👆',"\nHow many guesstions?",i)

    elif user_number > computer_number:
        print('Go Down 👇',"\nHow many guesstions?",i)

    elif user_number == computer_number:
        print('You Win 👏',"\nHow many guesstions?",i)
        break