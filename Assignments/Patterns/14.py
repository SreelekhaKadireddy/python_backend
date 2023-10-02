'''
1 2 3 4
1 2 3
1 2
1
'''
n=int(input("enter a value"))
for i in range(0,n):
    c = 1
    print(c, end=' ')
    for j in range(n - i - 1, 0, -1):
        c = c + 1
        print(c, end=' ')
    print(' ')