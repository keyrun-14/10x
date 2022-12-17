# n=int(input())
# arr=[]
# for i in range(n):
#     arr.append(int(input()))
# flag=-1
# for i in range(len(arr)):
#     count=0
#     for j in range(len(arr)):
#         if arr[j]>arr[i]:
#             count+=1
#     if count==arr[i]:
#         flag=1
#         break
# print(flag)


n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
arr.sort()
count=0
# arr=[1,2,3,3]
for i in range(len(arr)-1):
    if arr[i]>arr[i+1]:
        count+=1
    else:
        count=0
    if count==arr[i]:
        flag=1
        break

