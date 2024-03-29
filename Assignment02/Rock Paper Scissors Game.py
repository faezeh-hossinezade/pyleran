from random import randint
computer_score=0
user_score=0
while True:
    number = randint(1, 3)
    if number == 1:
        computer_choice = 'Rock'
    elif number == 2:
        computer_choice = 'Paper'
    elif number ==3:
        computer_choice = 'Scissors'

    user_choice = input('Choice Rock Or Paper Or Scissors Or Other For Exit: ').strip().title()
    print(f'Computer Choice: {computer_choice}')

    if user_choice == 'Rock' and computer_choice == 'Rock':
        print('Equal...','\nuser_score:',user_score,'\ncomputer_score:',computer_score)
    elif user_choice == 'Rock' and computer_choice == 'Paper':
        computer_score+=1
        print('You Lose','\nuser_score:',user_score,'\ncomputer_score:',computer_score)
    elif user_choice == 'Rock' and computer_choice == 'Scissors':
        user_score+=1
        print('You Win','\nuser_score:',user_score,'\ncomputer_score:',computer_score)
    elif user_choice == 'Paper' and computer_choice == 'Rock':
        user_score+=1
        print('You Win','\nuser_score:',user_score,'\ncomputer_score:',computer_score)
    elif user_choice == 'Paper' and computer_choice == 'Paper':
        print('Equal...','\nuser_score:',user_score,'\ncomputer_score:',computer_score)
    elif user_choice == 'Paper' and computer_choice == 'Scissors':
        computer_score+=1
        print('You Lose','\nuser_score:',user_score,'\ncomputer_score:',computer_score)
    elif user_choice == 'Scissors' and computer_choice == 'Rock':
        computer_score+=1
        print('You Lose','\nuser_score:',user_score,'\ncomputer_score:',computer_score)
    elif user_choice == 'Scissors' and computer_choice == 'Paper':
        user_score+=1
        print('You Win','\nuser_score:',user_score,'\ncomputer_score:',computer_score)
    elif user_choice == 'Scissors' and computer_choice == 'Scissors':
        print('Equal...','\nuser_score:',user_score,'\ncomputer_score:',computer_score)
        break

    else:
        print('Good By')
        break