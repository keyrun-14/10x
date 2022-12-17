# for i in range(int(input())):
#     arr=list(map(int,input().split()))
#     Sum=0
#     for i in range(len(arr)-2):
#         for j in range(i+1,len(arr)-1):
#             for k in range(j+1,len(arr)):
#                 if arr[i]+arr[j]>arr[k] and arr[j]+arr[k]>arr[i] and arr[k]+arr[i]>arr[j]:
#                     Sum=arr[i]+arr[j]+arr[k]
#     print(Sum)

# for i in range(int(input())):
#     arr=list(map(int,input().split()))
#     arr.sort(reverse=True)
#     Sum=0
#     for i in range(len(arr)-2):
#         if arr[i]+arr[i+1]>arr[i+2] and arr[i+1]+arr[i+2]>arr[i] and arr[i+2]+arr[i]>arr[i+1]:
#             Sum=arr[i]+arr[i+1]+arr[i+2]
#             break
#     print(Sum)



arr=[3,2,1,3,5]
arr2=sorted(arr)
print(arr)
print(arr2)

##[3, 2, 1, 3, 5]
##[1, 2, 3, 3, 5]
## 3
## soterd arr pairs =10