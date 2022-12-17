k=int(input())
people=input().split()
d={}
for i in people:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
arr=[]
for i in d:
    if d[i]>k:
        arr.append(i)

if len(arr)==0:
    print("no such names in this town!!!")
else:
    arr.sort()
    for i in arr:
        print(i)