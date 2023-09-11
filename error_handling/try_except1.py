a=20
b=10
c=0
r=a/b
print(r)
#r2=a/c #zeroDivisionError
try:
    r2=a/c
    print(r2)
except:
    print("division is not possible")