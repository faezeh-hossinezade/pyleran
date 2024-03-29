first_num = int(input('Enter first number: '))
second_num = int(input('Enter second number: '))

first_list = []
second_list = []

pos = second_num > first_num
if pos == False:
    great = first_list
    lower = second_list
else:
    great = second_list
    lower = first_list

for i in range(1,11):
    first_list.append(first_num * i)
    second_list.append(second_num * i)   

for i in range(first_num * second_num):
    if lower[i] in great:
        print("KMM is : ",lower[i])
        break 