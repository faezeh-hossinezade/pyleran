#give numbers
first_num = int(input("Enter first num: "))
second_num = int(input("Enter second num: "))

#loop
for i in range(1,first_num+1):
    if first_num % i == 0 and second_num % i == 0:
        bmm = i

print("B-M-M : ",bmm)