n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
##a.sort()
flag=-1
for i in range(n):
    count=0
    for j in range(n):
        if a[j]>a[i]:
            count=count+1
    if count==a[i]:
        flag=1
        break
print(flag)