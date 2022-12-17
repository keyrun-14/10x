# arr=list(map(int,input().split()))
# for i in range(1,len(arr)):
#     current=arr[i]
#     previous=i-1
#     while previous>=0 and current<arr[previous]:
#         arr[previous+1]=arr[previous]
#         previous-=1
#     arr[previous+1]=current
# print(arr)

# def mergesort(arr):
#     if len(arr)>1:
#         mid=len(arr)//2
#         left=arr[:mid]
#         right=arr[mid:]
#         mergesort(left)
#         mergesort(right)
#         i=j=k=0
#         while i<len(left) and j<len(right):
#             if left[i]<right[j]:
#                 arr[k]=left[i]
#                 i+=1
#                 k+=1
#             else:
#                 arr[k]=right[j]
#                 j+=1
#                 k+=1
#         while i<len(left):
#             arr[k]=left[i]
#             i+=1
#             k+=1
#         while j<len(right):
#             arr[k]=right[j]
#             j+=1
#             k+=1
#     return arr
# arr=list(map(int,input().split()))
# print(mergesort(arr))


def quicksort(arr):
    left=[]
    right=[]
    if len(arr)<1:
        return arr
    pivot=arr.pop(len(arr)//2)
    for i in range(len(arr)):
        if arr[i]<=pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return quicksort(left)+[pivot]+quicksort(right)
arr=list(map(int,input().split()))
print(quicksort(arr))