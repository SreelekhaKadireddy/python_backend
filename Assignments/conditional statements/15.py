#max of three nums
a = input("Enter a value: ")
b = input("Enter b value: ")
c = input("Enter c value: ")

max = 0

if a > b and a > c :
    max= a
elif b > c :
    smax = b
else :
    max = c

print(max, "is the max of three numbers.")