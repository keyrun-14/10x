l=list(map(int,input().split()))
m=int(input())
output=l[m:]+l[:m]
print(*output,sep="\n")