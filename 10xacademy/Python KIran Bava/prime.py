n=int(input("enter a no.    "))
count=0
for i in range(2,n):
        if ((n%i)==0):
                count=count+1
                break
if count==1:
            print(n,"is a prime number")
else:
            print(n,"is a non prime number")
