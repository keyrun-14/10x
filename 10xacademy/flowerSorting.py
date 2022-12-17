n=int(input())
flowers=list(map(int,input().split()))
for i in range(n):
    for j in range(i+1,n):
        if flowers[i]>flowers[j]:
            flowers[i],flowers[j]=flowers[j],flowers[i]
print(*flowers)