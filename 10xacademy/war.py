n,k=map(int,input().split())
arr = [[0 for i in range(n)] for j in range(n)]
counting=[]
for _ in range(k):
    i,j=map(int,input().split())
    for a in range(n):
        for b in range(n):
            if a==(i-1) or b==(j-1):
                for x in range(n):
                    arr[i-1][b] = 1               
                for y in range(n):
                    arr[a][j-1] = 1
    print(arr)
    count=0
    for i in range(n):
        for j in range(n):
            if arr[i][j]==0:
                count = count+1
    counting.append(count)
print(*counting)

