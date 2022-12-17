n=int(input("enter the no. of rows "))
a=0
for i in range(1,n+1):
	for j in range(1,n+1-i):
		print("x",end="")
		a+=1
	print("k"*a )  
