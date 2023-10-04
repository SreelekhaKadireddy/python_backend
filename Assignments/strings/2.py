'''
 Write a program that reads a string from keyboard and display:
* The number of uppercase letters in the string
* The number of lowercase letters in the string
* The number of digits in the string
* The number of whitespace characters in the string.
'''
str=input("enter a string:")
u=0
l=0
d=0
w=0
for i in str:
    if i.isupper():
        u+=1
    elif i.islower():
        l+=1
    elif i.isdigit():
        d+=1
    elif i==" ":
        w+=1
print("upper:",u)
print("lower:",l)
print("digits:",d)
print("white spaces:",w)