'''
program should create a new string by shifting one position to left.
For example if the user enters the string 'Pro Stack Academy' then
new string would be 'ro Stack AcademyP'
'''
s=input("enter a string:")
new_str=s[1:]+s[0]
print(new_str)