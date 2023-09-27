#find even nums from given nums
n=5
a=[]
for i in range(n):
    t=int(input())
    a.append(t)
for i in a:
    if i%2==0:
        print(i,end=" ")
