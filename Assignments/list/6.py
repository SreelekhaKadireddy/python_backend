#Remove empty strings from the list of strings
list1=eval(input("enter 1st list:"))
while ("" in list1):
    list1.remove("")
print (list1)