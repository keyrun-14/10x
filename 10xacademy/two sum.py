
a=list(map(int,input().split()))
target=int(input())
for i in range(len(a)):
    for j in range(len(a)):
        if i!=j:
            if a[i]+a[j]==target:
                if j>i:
                    print(i,j)
                          
#     if a[i]+a[i+1]==target:
#         print((a[i],a[i+1]))
# print(a) 