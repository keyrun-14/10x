n=int(input("enter the no. of rows "))
a=(-3)
for i in range(1,n+1):
	for j in range(1,n+1-i):
		print(" ",end="")
	a+=2
	print("k"*a)
	
