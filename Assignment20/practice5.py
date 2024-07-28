def is_palindrome(arr):
  n = len(arr)
  for i in range(n // 2):
    if arr[i] != arr[n - i - 1]:
      return False
  return True


my_list = [1, 4, 3, 4, 1]
print(is_palindrome(my_list))  # True

my_list = [1, 2, 3]
print(is_palindrome(my_list))  # False
