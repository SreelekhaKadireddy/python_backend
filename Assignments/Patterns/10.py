'''
A
B B
C C C
D D D D
'''
n=int(input())
for i in range (1,n+1):
    for j in range(1,i+1):
        print(chr(ord('A')+i-1),end=" ")
    print(' ')