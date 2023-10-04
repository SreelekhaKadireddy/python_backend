#iterate two lists simultaniously
list1=eval(input("enter 1st list:"))
list2=eval(input("enter 2nd list:"))
for (i,j) in zip(list1,list2):
    print(i,j)