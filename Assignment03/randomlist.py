from random import randint

numbers = []
end_point = 50
while True:
    user_input = int(input('Please Enter Number: '))
    if user_input > end_point:
        print(f'Please Enter a smaller number of {end_point}...')
    elif user_input < 0:
        print('Please Enter a larger number of {user input}...')
    else:
        break

while len(numbers) != user_input:
    random_number = randint(0, end_point)
    if random_number not in numbers: numbers.append(random_number)
print(numbers)