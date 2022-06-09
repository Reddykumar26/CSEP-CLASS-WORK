#1 remove duplicat eliments
"""
l1=[1,2,3,4,5,6,4,2,444,4]
l2=[]
for x in l1:
	if x not in l2:
		l2.append(x)
print(l2)
"""
#2 liner search present element  or  not and what location
"""
l=[1,2,3,4,5,2,6]
print(l)
ele=int(input("enter element to search :"))
c=0
if ele in l:
	for x in range(len(l)):

		if l[x]==ele:
			print(ele,"is present at",x,"position")
else:
	print(ele,"not in list")
"""

#3 [1,2,3,5,6,7,8] o/p=[1,2],[3,6]
"""
l1=[1,2,4,3,5,7,8]
print(l1)

l3=[]
for x in l1:
	l2=[]
	if x in l1 and 2*x in l1:
		l2.append(x)
		l2.append(2*x)
		l3.append(l2)
		del(l2)

print(l3)
"""
#4. mounatin

#1st method
"""
l1=[1,2,2,3,3,4,3,2,2,2,2,2,1]
print(l1)
l2=[]
l3=[]
n=len(l1)
k=int(max(l1))
m=l1.index(k)
print(m)
for x in range(m):
	l2.append(l1[x])
print(l2)
l2.sort()

for x in range(m,n):
	l3.append(l1[x])
print(l3)
l3.sort()


l4=l3[::-1]
l5=l2+l4		


if l1==l5:
	print("mountain array")
else:
	print("not mountain")
"""
# 2nd method	
"""
l1=[1,2,3,4,5,6,7,8,3,2,1]
print(l1)
l=int(len(l1))
print("length",l)
m=int(max(l1))
index=int(l1.index(m))
print("index",index)
l2=l1[:index]
print(l2)
l2.sort()
l3=l1[-1:index:-1]
l3.sort()
l3=l3[::-1]	
print(l3)
l4=l2+l3
l4.insert(index,m)
print(l4)
if l1==l4:
	print("MOUNTAIN LIST")
else:
	print("NOT MOUNTAIN LIST")
"""
#3rd method Equilateral mountain list or not
l1=[1,2,2,2,2,2,2,2,3,4,3,2,2,2,2,2,2,2,1]
print(l1)
l=int(len(l1))

print("length",l)
m=int(max(l1))
index=int(l1.index(m))
print("index",index)

l2=l1[:index]
print(l2)
l2.sort()
l3=l1[-1:index:-1]
l3.sort()
l3=l3[::-1]	
print(l3)
l4=l2+l3
l4.insert(index,m)
print(l4)
if l1==l4 :
	if l4[:index]==l4[-1:index:-1]:
		print("EQUILATERAL  MOUNTAIN LIST")
	else:
		print("NOT EQUILATERAL MOUNTAIN LIST")
else:
	print("NOT A  MOUNTAIN LIST")

# construct a mountain list from the elemenst in list
"""
l1=[1,2,2,0,3,9,39]
print(l1)
l1.sort()
len=int(len(l1))
if len%2!=0:
	len=len-1
	l=int(len/2)
	l2=l1[:l]
	l3=l1[l::]
	l3=l3[::-1]
	l3=l2+l3
	print("possible")
	print(l3)
	
else:
	print("NOT POSSIBLE")
"""

