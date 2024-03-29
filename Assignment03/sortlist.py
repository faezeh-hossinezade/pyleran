import re
array = input("Enter array Like: 1,2,3 :")
array_member = re.split(",",array)
check_validator = 0
for i in range(len(array_member)):
    if int(array_member[i])>check_validator:
        check = int(array_member[i])
        if i == len(array_member) -1 :
            print("Array is an ordered")
    else:
        print("Array is not an ordered")
        break