'''
Write a program which will find all such numbers which are divisible by 7
but are not a multiple of 5, between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''
l=int(input("enter lower limit:"))
u=int(input("enterupper limit:"))
for num in range(l,u+1):
    if num%7==0 and num%5!=0:
        print(num,end=",")