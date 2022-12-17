n=int(input())
arr=list(map(int,input().split()))
d={}
for i in range(n):
    d[arr[i]]=i
count=0
for i in range(n):
    if arr[i]-1 not in d:
        k=arr[i]
        while k in arr[d[k]:]:
            k+=1            
        if count<(k-arr[i]):
            count=(k-arr[i])            
print(count)


# n=int(input())
# arr=list(map(int,input().split()))
# count=0
# for i in range(n):
#     if arr[i]-1 not in arr:
#         k=arr[i]
#         while k in arr[i:]:
#             k+=1
#         if count<(k-arr[i]):
#             count=(k-arr[i])
# print(count)

        

# 10
# 4 -5 0 1 -2 2 -1 3 -4 -3