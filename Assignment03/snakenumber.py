num = int(input('Please Enter Your Number: '))
for i in range(num):
    if i % 2 == 0:
        print('*', end='')
    else:
        print('#', end='')