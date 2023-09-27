#min of 3 nums using ternary operator
a = input("Enter a value: ")
b = input("Enter b value: ")
c = input("Enter c value: ")
print(a) if (a<b and a<c) else (print(b) if b<c else print(c))