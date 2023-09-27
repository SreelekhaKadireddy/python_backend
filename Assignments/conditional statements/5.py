#check a number is positive or not
num=int(input())
if num==0:
    print("enter a valid number:")
    num=int(input())
elif num>0:
    print("positive number")
else:
    print("not a positive number(negative)")