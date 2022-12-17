n=int(input())
a=[]
b=0
for i in range(1,n+1):
    b=n%i
    if b==0:
        a.append(b)
if len(a)>2:
    print("No")
  
else:
    print("Yes")

 