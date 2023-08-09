#list methods
l=[10,20,40]
l.append(50)
l.insert(2,30)
l.extend(['a','b','c'])
print(l)
print(l)
print(l)
l.remove(10)
print(l)
l.pop()
print(l)
del l[1]
print(l)
l.clear()
print(l)
#l1=eval(input())
#print(l1)
l2=['a','b','c','d','e']
for item in l2:
    print(item)
i=0
while i<len(l2):
    print(l2[i])
    i+=1
l2.append('f')
print(l2)
#new_list=[x for x in l2 and x in {'a','b','c'}]
#print(new_list)
newList=[i.upper() for i in l2]
print(newList)
l3=[30,40,20,19]
l3.sort()
print(l3)
l3.sort(reverse=True)
print(l3)
l4=["Apple","bat","Umbrella","Xyz"]
l4.sort()
print(l4)#case sensitive
l4.reverse()
l5=l4.copy()
print(l5)
l6=list(l3)
print(l6)
l7=l5+l4
print(l7)#joining 2 lists


