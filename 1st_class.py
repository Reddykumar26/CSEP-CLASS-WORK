"""
1.
# index out of range
l=[10,20,11,23,30,40,50]
k=int(len(l))
i=int(input("enter index :"))
if i<k:
	print(l[i])
else:
	print("Index out of range")




2.
#copy list into another list
list1=[10,20,40,2,1]
list2=[-2,50,0,20,4]
list1.extend(list2)
print(list1)
print(sorted(list1))


3.
list1=[1,2,0,4]
print(list1)
index=list1.index(0)
list1.insert(index,0)
print(list1)
"""
4.
list1=[1,2,3,0,4,0,5]
list2=[]
print(list1)
for x in list1:
	if x==0:
		list2.append(x)
		list2.append(x)
	else:
		list2.append(x)
print(list2)





 
