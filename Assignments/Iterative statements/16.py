#reverse the digits of given number
n=int(input())
new=0
while n%10!=0:
    rem=n%10
    new=new*10+rem
    n=n//10
print(new)
