'''''
    # your code goes here
A,B=input().split()
A,B=int(A),int(B)
num=0
for i in range(1,4):
     c=i  
     num=A*B*c
     break 
if (num%2)!=0:
    print("yes")
else:
    print("no")
'''''
A,B=input().split()
A,B=int(A),int(B)
num=A*B
if num%2!=0:
    print("yes")
else:
    print("no")