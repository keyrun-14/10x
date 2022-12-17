n=int(input())
print("*"*((2*n)-1))
for i in range(1,n):
    print("*"*(n-i)+" "*((i-1)+i)+"*"*(n-i))
    
