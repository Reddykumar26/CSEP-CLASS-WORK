#factorial

def fact(n):
	return 1 if(n==1 or n==0) else n*fact(n-1)
n=int(input("enter a number : "))
fact(n)
print("factotial is : ",fact(n))

	
