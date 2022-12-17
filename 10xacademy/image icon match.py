n=int(input())
a=[]
count=0
for i in range(n):
    a.append(int(input()))

m=int(input())
b=[]
for i in range(m):
    b.append(int(input()))
if m==0:
    print(0)
elif m==1:
    print(a.count(b[0]))

elif m==2:
    for i in range(n-1):
        if a[i]==b[0] and a[i+1]==b[1]:
            count+=1
           
    print(count)
    

