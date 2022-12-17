# for i in range(int(input())):
#     arr=list(map(int,input().split()))
#     for j in range(1,len(arr)):
#         if arr.count(arr[j])==1:
#             print(arr[j])
#     if arr.count(arr[0])-1==1:
#         print(arr[0])

# for i in range(int(input())):
#     arr=list(map(int,input().split()))
#     for j in range(1,len(arr)):
#         if arr.count(arr[j])==1:
#             print(arr[j])
#     if arr.count(arr[0])-1==1:
#         print(arr[0])

# for i in range(int(input())):
#     arr=list(map(int,input().split()))
#     b=arr[1:]
#     b.sort()
#     count=0
#     if len(arr)==2:
#         print(arr[1])
#     elif b[0]^b[1]!=0:
#         print(b[0])
#     else:
#         for j in range(len(b)-1):
#             a=b[j]^b[j+1]
#             if a==0:
#                 count=0
#             if a!=0:
#                 count+=1
#             if count==2:
#                 print(b[j])
#                 break
#             if count==1 and j+1==len(b)-1:
#                 print(b[j+1])

for i in range(int(input())):
    arr=list(map(int,input().split()))
    count=0
    if len(arr)==2:
        print(arr[1])
    else:
        x=0
        for i in range(1,len(arr)):
            x=x^arr[i]
        print(x)
           
# 1
# 22 1 2 3 4 5 6 7 8 9 10 11 1 2 3 4 5 6 7 8 9 10