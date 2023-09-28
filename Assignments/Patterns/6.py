'''
5 5 5 5 5
4 4 4 4 4
3 3 3 3 3
2 2 2 2 2
1 1 1 1 1
'''
n=int(input())
for i in range(n,0,-1):
    for j in range (n):
        print(i,end=" ")
    print(" ")