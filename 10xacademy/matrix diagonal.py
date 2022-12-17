n=int(input())
b=[]
for x in range(n):
    a=list(map(int,input().split()))[:n]
    b.append(a)
i=0
j=0
while i<n and j<n:
    if b[i][j]<0:
        b[i][j]=0
    elif b[i][j]>=0:
        b[i][j]=1
    i=i+1
    j=j+1
for c in range(n):
    print(b[c])
# a=[1,2,3,4,5]
# b=[[1,2,3],[4 5 6],[7 8 9]]
# a[4]=5
# a[2]=3
# b[0][2]=3
# 12 3 4    0,2
# 5 6 7       1,1
# 8 9 0           2,0      2,2
# 3*3

# n=3
# i=0
# j=n-1
#  while i<n and j>=0
#     i=i+1
#     j=j-1
