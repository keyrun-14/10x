# n,k = map(int,input().split())
# final_array=[]
# for i in range(n):
#     arr=input()
#     final_array.append(list(arr))
# flag=0
# count=0
# i=0
# j=0

# while j<k:
#     i=0
#     while i<n:
#         if final_array[i][j]<final_array[i+1][j]:
#             flag=1
#             i+=1
#         else:
#             flag=0
#             break
#     j+=1
#     if flag==0:
#         count+=1
# print(count)



n,k = map(int,input().split())
final_array=[]
for i in range(n):
    arr=input()
    final_array.append(list(arr))
zip(final_array)
print(final_array)
# flag=0
# count=0

# for j in range(k):
#     i=0
#     while i<n:
#         if final_array[i][j]<final_array[i+1][j]:
#             flag=1
#             i+=1
#         else:
#             flag=0
#             break

#     if flag==0:
#         count+=1
# print(count)

# 3 4
# adsf
# bfax
# yzzu