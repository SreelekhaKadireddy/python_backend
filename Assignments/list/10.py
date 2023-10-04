#Remove all occurrences of a specific item from a list.
def remove(l,a):
    new_list=[i for i in l if i!=a]
    return new_list

l=eval(input("enter list items:"))
a=eval(input("enter an item:"))
print(remove(l,a))