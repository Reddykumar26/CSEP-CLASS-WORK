list1=eval(input( "enter list :"))
# bubble sort
for i in range(len(list1)-1):
	for j in range(len(list1)-(i+1)):
		if list1[j] > list1[j+1]:
			t=list1[j+1]
			list1[j+1]=list1[j]
			list1[j]=t

print("list is sorted")
print(list1)

#binay search

start=0
end=len(list1)


c=0	
k=eval(input("enter value to check :"))
for index in  range(len(list1)):
	mid= (start + end) //2
	

	if k==list1[mid]:
		c=c+1
		break
	if k <	list1[mid]:

		end=mid-1
	else:
		start=mid+1
	
	
	
	
if c==0:
	print("not present")
else:
	print("present")
