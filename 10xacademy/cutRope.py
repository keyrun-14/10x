# n=int(input())
# arr=[]
# temp=[]
# for i in range(n):
#     arr.append(int(input()))
# while len(arr):
#     minn=min(arr)
#     for j in range(len(arr)):    
#         k=arr[j]-minn
#         if k>0:
#             temp.append(k)
#     arr=temp
#     if len(arr)>0:
#         # print(arr)
#         print(len(arr))
#     temp=[]



n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)
while len(arr):
    minn=arr[-1]
    for j in range(len(arr)):
        arr[j]=arr[j]-minn
    for k in range(len(arr)-1,-1,-1):
        if arr[k]<=0:
            arr.pop()
        else:
            break
    if len(arr)>0:
        print(len(arr))

# arr=[1,2,3,4]
# arr.pop(2)
# print(arr)
# arr.remove(2)  
# print(arr)
    

# def quicksort(arr):
#     left = []
#     right = []
#     if len(arr) < 1:
#         return arr
#     pivot = arr.pop(len(arr)//2)
#     count=0
#     minn=0
#     for i in range(len(arr)):
#         if arr[i] <= pivot:
#             minn = arr[i]-min(arr)
#             if minn>0:
#                 count=count+1
#             left.append(arr[i])
#         else:
#             count=count+1
#             right.append(arr[i])
        
#     if count>0:
#         print(count)
#     return quicksort(left)+[pivot]+quicksort(right)
# n=int(input())
# arr = list(map(int, input().split()))
# print(*quicksort(arr))