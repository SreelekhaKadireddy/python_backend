#conditional flow(if,if-else,if-elif-else)
a=int(input())
b=int(input())
print(a if a>b else b,"is bigger number")
c=int(input())
if a>b and a>c:
    print("a is bigger")
elif b>a and b>c:
    print("b is bigger")
else:
    print("c is bigger")
#iterative flow(while,for)
l=[10,20,30,40]
for i in l:
    print(i)
x=0
while x<=10:
    print(x)
    x+=1
for i in range(10):
    print(i)
for i in range(10,0,-2):
    print(i)