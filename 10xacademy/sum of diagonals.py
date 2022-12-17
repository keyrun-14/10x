m=int(input())
matrix=[]
for i in range(m):
    matrix.append(list(map(int,input().split()))[:m])
i,j=0,0
left_diagonal=0
while i<m and j<m:
    left_diagonal=left_diagonal+matrix[i][j]
    i=i+1
    j=j+1

x,y=0,m-1
right_diagonal=0
while x<m and y>=0:
    right_diagonal=right_diagonal+matrix[x][y]
    x=x+1
    y=y-1

print(left_diagonal+right_diagonal)