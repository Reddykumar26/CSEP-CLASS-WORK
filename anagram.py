

#	anagram string
str1= eval(input("enter first string :"))
str2= eval(input("enter second string :"))

"""
#	METHOD 1
str1=sorted(str1)
str2=sorted(str2)
if str1==str2:
	print("yes")
else:
	print("no")
	
"""
"""
#	METHOD 2

if len(str1)!=len(str2):
	print("no")
else:
	c=0
	for i in str1:
		if str1.count(i) == str2.count(i):
			c=c+1
	if c==len(str1):
		print("yes")
	else:
		print("no")
"""

#	METHOD 3

c=0
dict1={}
dict2={}
for i in str1:
	dict1[i]=str1.count(i)
print(dict1)		
print()
for i in str2:
	dict2[i]=str2.count(i)
print(dict2)

if len(str1)!=len(str2):
	print("no")
else:		
	for k in dict1.keys():
		if  k in dict2 and dict1[k]==dict2[k]:
			c=c+1
	if c==len(dict1):
		print('yes')
	else:
		print('no')
	

				
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
