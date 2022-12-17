def slice_matrix(L,R,T,B):
    if L<=R and T<=B:
        for i in range(T-1,B):
            # x=[]    
            for j in range(L-1,R):
                output=matrix[i][j]
                print(output,end=" ")
            print()
            #     x.append(output)            
            # print(*x)   
m,n=map(int,input().split())
matrix=[]
for i in range(m):
    a=list(map(int,input().split()))[:n]
    matrix.append(a)
L,R,T,B=map(int,input().split())
slice_matrix(L,R,T,B)
# m=3
# n=1
# matrix=[]
# for i in range(m):
#     a=list(map(int,input().split()))[:i+1]
#     matrix.append(a)
# print(matrix)