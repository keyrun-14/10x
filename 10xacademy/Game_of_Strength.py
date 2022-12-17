# # for i in range(int(input())):
# #     n = int(input())
# #     arr = list(map(int, input().split()))
# #     sum = 0
# #     for j in range(len(arr)-1):
# #         for k in range(j+1, len(arr)):
# #             sum = sum+max(arr)*abs((arr[j]-arr[k]))
# #     print(sum)
# summ=0
# arr=[1,2,3,4,5]
# for x in range(len(arr)):
#     summ = (summ+((arr[x]*x)-(arr[x]*(len(arr)-x-1))))
#     print((arr[x]*x))
#     print((arr[x]*(len(arr)-x-1)))
#     print(summ)
#     print()

# your code goes
# def gameOfStrength(arr, lowerBound, upperBound):
#     if lowerBound < upperBound:
#         mid = (lowerBound+upperBound)//2
#         gameOfStrength(arr, lowerBound, mid)
#         gameOfStrength(arr, mid+1, upperBound)
#         merge(arr, lowerBound, mid, upperBound)
# def merge(arr, lowerBound, mid, upperBound):
#     temp = [0]*(upperBound-lowerBound+1)
#     i = lowerBound
#     j = mid+1
#     k = 0
#     while i <= mid and j <= upperBound:
#         if arr[i] < arr[j]:
#             temp[k] = arr[i]
#             i = i+1
#         else:
#             temp[k] = arr[j]
#             j = j+1
#         k = k+1
#     while i <= mid:
#         temp[k] = arr[i]
#         i = i+1
#         k = k+1
#     while j <= upperBound:
#         temp[k] = arr[j]
#         j = j+1
#         k = k+1
#     for x in range(lowerBound, upperBound+1):
#         arr[x] = temp[x-lowerBound]
# for t in range(int(input())):
#     n = int(input())
#     arr = [int(x) for x in input().split()]
#     gameOfStrength(arr, 0, len(arr)-1)
#     summ = 0
#     for x in range(len(arr)):
#         summ = (summ+((arr[x]*x)-(arr[x]*(len(arr)-x-1))))
#     result = summ*max(arr)
#     print(result%1000000007)

# def gameOfStrength(arr, lowerBound, upperBound):
#     if lowerBound < upperBound:
#         mid = (lowerBound+upperBound)//2
#         gameOfStrength(arr, lowerBound, mid)
#         gameOfStrength(arr, mid+1, upperBound)
#         merge(arr, lowerBound, mid, upperBound)
# def merge(arr, lowerBound, mid, upperBound):
#     temp = [0]*(upperBound-lowerBound+1)
#     i = lowerBound
#     j = mid+1
#     k = 0
#     while i <= mid and j <= upperBound:
#         if arr[i] < arr[j]:
#             temp[k] = arr[i]
#             i = i+1
#         else:
#             temp[k] = arr[j]
#             j = j+1
#         k = k+1
#     while i <= mid:
#         temp[k] = arr[i]
#         i = i+1
#         k = k+1
#     while j <= upperBound:
#         temp[k] = arr[j]
#         j = j+1
#         k = k+1
#     for x in range(lowerBound, upperBound+1):
#         arr[x] = temp[x-lowerBound]
# for t in range(int(input())):
#     n = int(input())
#     arr = [int(x) for x in input().split()]
#     gameOfStrength(arr, 0, len(arr)-1)
#     summ = 0
#     for x in range(len(arr)):
#         summ = (summ+((arr[x]*x)-(arr[x]*(len(arr)-x-1))))
#     result = summ*max(arr)
#     print(result%1000000007)

# def mergeSort(arr):
#     if len(arr) > 1:
#         mid = len(arr)//2
#         L = arr[:mid]
#         R = arr[mid:]
#         mergeSort(L)
#         mergeSort(R)
#         i = j = k = 0
#         while i < len(L) and j < len(R):
#             if L[i] < R[j]:
#                 arr[k] = L[i]
#                 i += 1
#             else:
#                 arr[k] = R[j]
#                 j += 1
#             k += 1
#         while i < len(L):
#             arr[k] = L[i]
#             i += 1
#             k += 1
#         while j < len(R):
#             arr[k] = R[j]
#             j += 1
#             k += 1 
# for i in range(int(input())):
#     n=int(input())
#     arr = list(map(int,input().split()))
#     mergeSort(arr)
#     summ = 0
#     for x in range(len(arr)):
#         summ = (summ+((arr[x]*x)-(arr[x]*(len(arr)-x-1))))
#         # print((summ," + ",((arr[x]," * ",x)," - ",(arr[x]," * ",(len(arr)," - ",x," - ",1)))))
#         print(summ)
#     result = summ*max(arr)
#     print(result%1000000007)

# for i in range(int(input())):
#     n=int(input())
#     arr = list(map(int,input().split()))
#     arr.sort()
#     summ = 0
#     for x in range(len(arr)):
#         summ = summ+arr[x]*
#         # print((summ," + ",((arr[x]," * ",x)," - ",(arr[x]," * ",(len(arr)," - ",x," - ",1)))))
#         print(summ)
#     result = summ*max(arr)
#     print(result%1000000007)

x=3
x+=4.6
print(x)
x=x+4.6
print(x)