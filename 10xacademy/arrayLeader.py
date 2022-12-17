n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
last=arr[n-1]
print(arr[n-1])
for i in range(n-2,-1,-1):
    if last<arr[i]:
        print(arr[i])              
        last=arr[i]                  

# arr=[1,2,3,4,5,6,7,8,9,10]
# print("length of array ",len(arr))
# for i in range(len(arr)):
#     print(arr[i],end=" ")
# print()
# for i in range(len(arr)-1,-10,-1):
#     print(arr[i],end=" ")

#     length of array  10
# 1 2 3 4 5 6 7 8 9 10 

# 10 9 8 7 6 5 4 3 2 1 