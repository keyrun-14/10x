'''''''''''
n,k=input().split()
n,k=int(n),int(k)
count=0
while n>2:
    n=n-k
    count+=1
if n==1:
    print(count)
else:
    print(-1)
'''''''''
'''''
n,k=input().split()
n,k=int(n),int(k)
#count=0
while n>=2:
    n=n-k
    #count+=1
if n==1:
    print("count")
else:
    print(-1)
'''
n=int(input())
for i in range(n):
    k=int(input())
    if k>2:
        print(1)
    elif k==1:
        print(0)
    else:
        print(-1)