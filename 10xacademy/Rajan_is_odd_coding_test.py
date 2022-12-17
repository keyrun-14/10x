# from collections import Counter
# n=int(input())
# arr=list(map(int,input().split()))[:(2*n+1)]
# dict=Counter(arr)
# for i in dict:
#     if dict[i]%2 != 0:
#         print(i)


n=int(input())
arr=list(map(int,input().split()))[:(2*n+1)]
k=0
for i in arr:
    k=k^i
print(k)