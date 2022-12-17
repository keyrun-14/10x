n=int(input())
arr=list(map(int,input().split()))
d={}
for i in arr:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
output='NONE'
for key ,value in d.items():
    if value>n//2:
        output=key
print(output)
