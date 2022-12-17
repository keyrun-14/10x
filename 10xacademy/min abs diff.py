# n=int(input())
# a=list(map(int,input().split()))[:n]
# s=[]
# diff=0
# for i in range(0,n-1):
#     for j in range(i+1,n):
#         diff=abs(a[i]-a[j])
#         s.append(diff)
# print(min(s))
n=int(input())
a=list(map(int,input().split()))[:n]
s=[]
diff=0
a.sort()
for i in range(1,n):
    diff=abs(a[i-1]-a[i])
    s.append(diff)
print(min(s))

n=int(input())
a=list(map(int,input().split()))[:n]
diff=0
mindiff=float('inf')
a.sort()
for i in range(n-1):
    small=a[ai]
    large=a[i+1]
    diff=large-small
    if diff<mindiff:
        mindiff=diff
print(mindiff)