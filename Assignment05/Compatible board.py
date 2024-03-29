def chessboard(n,m):
    for i in range(n): #we add 0 and 1 as much as we have n
        for j in range(m):
            if (i+j)%2 == 0: #
                print('#',end='')
            else:
                # row.append("*")
                print('*' , end='')
        print()




n=int(input('Enter Number of rows:'))
m=int(input('Enter Number of columns:'))
chessboard(n,m)