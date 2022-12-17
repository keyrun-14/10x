n=int(input())
a=[]
sum=0
for i in range(n):
    ele=int(input())
    a.append(ele)
    if a[i]>0:
        sum=sum+a[i]
print(sum)