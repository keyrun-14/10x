n=int(input())
arr=list(map(int,input().split()))
d={}
sum=0
for i in range(n):
    d[arr[i]]=abs(arr[i]-(i+1))
    sum+=abs(arr[i]-(i+1))
print(d)
print()
print(sum)
d.values.sort()
print(d.values)