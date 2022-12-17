# your code goes here
from collections import Counter
n=int(input())
arr=[int(x) for x in input().split()]# 1 3 3 4 5
arr.sort()
count=Counter(arr) #
#print(count)
# print(count)
# 8
# 1 2 3 4 4 5 5 5
# Counter({5: 3, 4: 2, 1: 1, 2: 1, 3: 1})
flag=1
for i in range(2,arr[-1]+1):#
    if count[i]>count[i-1]:
        flag=2
        break
if flag==1:
    res=[]
    for i in range(arr[-1],0,-1):
        temp=[]
        val=count[i]
        if val>0:
            for j in range(1,i+1):
                temp.append(j)
                count[j]-=val
            for k in range(val):
                res.append(temp)
    print(len(res))
    for i in reversed(res):
        print(*i)
else:
    res=0
    threshold=0
    for i in range(arr[-1],0,-1):
        if count[i]>=threshold:
            threshold=count[i]
        else:
            diff=threshold-count[i]
            count[i]+=diff
            res+=diff
    print(res)