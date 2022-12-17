# n=int(input())
# k=int(input())
# arr=[]
# for _ in range(k):
#     b=0
#     i,j=map(int,input().split())
#     arr.append(i)
#     arr.append(j)
#     print(len(arr))
#     print(arr)
#     while len(arr)>=b:
#         if arr[b]==j:
#             arr[b]=i
#         b+=1
#     print(arr)
# print(arr)


# # n=int(input())
# # k=int(input())
# # for _ in range(k):
# #     i,j=map(int,input().split())
# # print(n-k)
n=int(input())
arr=list(map(int,input().split()))
i,x,y,ans=0,0,0,0
mm=[]
a=[0]*n
for i in range(n):
    mm[arr[i]]+=1
# for i in range(mm):
print(mm)
