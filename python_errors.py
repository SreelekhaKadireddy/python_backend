#python errors production
#1.Type error:when operation is performed on incorrect/unsupported objects

a=int(input())
b=str(input())
print(a+b)

#2.Value error:when a value is invalid for a given operation
import math
c=int(input())
sol=math.sqrt(c)
print(sol)

#3.Nameerror: when object is not found or function is not defined
def add():
    pass
add_1()

#4.Index error: when try to access element of invalid index in a sequence
l=[1,2,3,4,5]
print(l[1])
print(l[-3])
print(l[10])

#5.Attribute error: when attribute reference or assignment fails
num=10
print(type(num))
num.append(10)
print(num)

#6.syntax error:when proper syntax of code is not followed
_@name=input()
print(_@name)
def with():
    pass
with()

#7.ZeroDivisionError:when you divide a value or variable with zero
num1=20
num2=0
ans=num1/num2
print(ans)

#8.key error:when you try to access a key that is not in dict
dic={"name":"siri","id":100,"sal":45000}
print(dic["name"])
print(dic["exp"])

#9.EOF error:end of file exception in python when input() fuction hits EOF condition
try:
    n = int(input())
    print(n * 10)
    
except EOFError as e:
    print(e)

#10.Indentation error:raises when there is incorrect indentation
def fun1():
pass
fun1()

#11.Runtime error:when an error does not fall under any other category of python built in errors
'''
division by zero
performing an operation on incompatible types
using an identifier that has not been defined
accessing a list element, dictionary value, or object attribute which doesn’t exist
trying to access a file that doesn’t exist
'''
#12.Assertion error
#13.system error
#14.memory error
#15.overflow error
#16.arithmetic error
#17.floating point error
#18. IO error
#19.Reference error
#20. OS error
