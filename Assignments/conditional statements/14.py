#min of three nums
a = input("Enter a value: ")
b = input("Enter b value: ")
c = input("Enter c value: ")

smallest = 0

if a < b and a < c :
    smallest = a
elif b < c :
    smallest = b
else :
    smallest = c

print(smallest, "is the min of three numbers.")