#program to count and display the number of vowels in a given string?
str=input()
vowels=['a','e','i','o','u','A','E','I','O','U']
c=0
for i in str:
    if i in vowels:
        c+=1
        print(i,end=" ")
print("\n",c)