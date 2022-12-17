r,c=input().split()
r,c=int(r),int(c)
m=[]
a=[]
for i in range(r):
    b = [int(x) for x in input().split()]
    a.append(b)
sum=0
for i in range(r):
    for j in range(c):
        if (a[i][j])%2!=0:
            sum=sum+a[i][j]
print(sum)