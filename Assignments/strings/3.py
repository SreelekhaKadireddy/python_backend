'''
Your program should create and display a new string where the first and last
characters have been exchanged.
For example if the user enters the string 'HELLO' then new string would be
'OLEEH'
'''
s=input("enter a string:")
new_s=s[-1]+s[1:-1]+s[0]
print(new_s)
