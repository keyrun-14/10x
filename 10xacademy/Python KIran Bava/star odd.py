n=int(input("enter the no. of rows "))
a=1
for i in range(1,n+1):
	for j in range(1,n+1-i):
		print(" ",end="")
	print("k"*a)
	a+=2