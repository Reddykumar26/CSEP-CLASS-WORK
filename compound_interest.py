#compund interest
p = eval(input("enter principal amount : "))
r = eval(input("enter rate of interest : ")) 
t = eval(input("enter time in years : "))
if t==0:
	print("enter valid time")
else:
	a = p*(pow((1+(r/100)),t))
	print("total amount : ",a)
	print("compound interest : ",a-p)

