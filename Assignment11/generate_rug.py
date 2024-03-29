import numpy as np


def generate_rug(n):
    carpet = np.array([[0] * n] * n)
    # print (carpet)
    n = n // 2

    def select(start, end, num):
        for i in range(start, end + 1):
            for j in range(start, end + 1):
                carpet[i, j] = num
    
    for num in range(n, -1, -1):
        select(n - num, n + num, num)

    return carpet
            
def show(carpet):
    for row in carpet:
        print(row)


x=int(input("Enter the number: "))
if x%2==0:
    print(" OOPS! ") 
else:
    carpet = generate_rug(x)
    show(carpet)
        