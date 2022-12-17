n = int(input())
a= list(map(int,input().split()))
sum=0
for i in range(0,n):
    sum=sum+a[i]
avg=sum/n
print(int(avg))
