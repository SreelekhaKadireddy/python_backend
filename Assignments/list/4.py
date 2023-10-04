#Concatenate two lists in the following order
list1=eval(input("enter 1st list:"))
list2=eval(input("enter 2nd list:"))
for item in list2:
    list1.append(item)
print(list1)