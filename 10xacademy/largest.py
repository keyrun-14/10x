def largest(n,a):
    temp=0
    for i in range(n-1):
        for j in range(i+1,n):
            if a[i]>a[j]:
                temp=a[j]
                a[j]=a[i]
                a[i]=temp    
    return (a[-1])
n=int(input())
a=list(map(int,input().split()))[:n]
print(largest(n,a))