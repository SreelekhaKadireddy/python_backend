'''square pattern with 
1 1 1 1
2 2 2 2
3 3 3 3
4 4 4 4
'''
n=int(input())
for i in range(n):
    for j in range(n):
        print(i+1, end=" ")
    print(" ") 