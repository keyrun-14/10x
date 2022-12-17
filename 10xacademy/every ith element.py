n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
i=int(input())
sum=0
for x in range(i-1,n,i):
    sum=sum+a[x]
print(sum)
