#Write a program which can compute the factorial of a given number
def factorial(n):
    if n==0 or n==1:
        return 1
    elif n<0:
        return "enter a positive number"
    else:
        return n*factorial(n-1)
    
n=int(input("enter a number:"))
print(factorial(n))
