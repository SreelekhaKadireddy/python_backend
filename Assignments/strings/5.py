'''
Write a program that display following output: input - stack
● stack
● tacks
● ackst
● cksta
● kstac
'''
def output(s):
     res = []
     n = len(s)
     for i in range(0, n):
        s = s[1:n]+s[0]
        res.append(s)
     return res

s=input("enter a string:")
res=output(s)
for item in res:
    print(item)