#Add new item to list after a specified item
l=eval(input("enter list of items:"))
i=int(input("enter index number:"))
n=input("enter what you have to insert:")
if i==len(l)-1:
    l.append(n)
else:
    l.insert(i+1,n)
print(l)