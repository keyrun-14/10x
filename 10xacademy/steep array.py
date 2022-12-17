# n=int(input())
# sum=0
# b=[int(n) for n in input(). split ()]
# for i in range(n-1,-1,-1):
#     sum=sum+(max(b[i:])-b[i])
# print(sum)

n=int(input())
sum=0
b=[int(n) for n in input(). split ()]
maxm=b[n-1]
for i in range(n-1,-1,-1):
    maxm=max(maxm,b[i])
    sum=sum+maxm-b[i]
print(sum)