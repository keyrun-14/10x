n=int(input())
arr=[]
flag=0
for i in range(n):
    arr.append(int(input()))
if n<=0:
    print(-1)
elif n>1:
    count=1
    for i in range(n-1):
        if arr[i]==arr[i+1]:
            count=count+1
        if count==arr[i]:
            print(arr[i])
            flag=1     
            break
        elif arr[i]!=arr[i+1]:
            count=1
    if flag==0:
        print(-1)
elif n==1 and arr[0]==1:
    print(1)
else:
    print(-1)