import re

numbers=input('Please Enter array Like 1,2,3,4,5: ')
numbers_array=re.split(',',numbers)
unique_list=[]

for i in range(len(numbers_array)):
    if numbers_array[i] not in unique_list:
        unique_list.append(numbers_array[i])
        
        
print (unique_list)
        

