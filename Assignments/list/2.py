#concatinate 2 lists index wise
list1=eval(input("enter 1st list:"))
list2=eval(input("enter 2nd list:"))
new_list=[i+j for i,j in zip(list1,list2)]
print("new concatination list is:"+str(new_list))
