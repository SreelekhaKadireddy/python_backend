'''
A
A B
A B C
A B C D
'''
n=int(input("enter a value"))
for i in range(n):
    for j in range(i+1):
        print(chr(ord('A')+j),end=" ")
    print(" ")