#Replace list’s item with new value if found
l=eval(input("enter list items:"))
a=eval(input("enter an item:"))
rep=eval(input("enter new element:"))
for x in range(len(l)):
    if l[x]==a:
        l[x]=rep
    
print(l)