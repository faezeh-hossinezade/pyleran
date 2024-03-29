import re
array = input("Enter array Like: 1,2,3 :")
array_member = re.split(",",array)

left = 0
right = len(array_member)-1

while (left < right):
        # Swap
        temp = array_member[left]
        array_member[left] = array_member[right]
        array_member[right] = temp
        left += 1
        right -= 1
        
print(array_member)