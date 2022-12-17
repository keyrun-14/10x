n=int(input())
b=[]
for i in range(n):
    b.append(list(map(int,input().split()))[:n])
i=0
j=n-1
while i<n and j>=0:
    print(b[i][j])
    i=i+1
    j=j-1
