n=int(input())
a=[]
for i in range(n):
    b=int(input())
    a.append(b)
for i in a:
    count=a.count(i)
    if count==4:
        print(a[i])
        break
else:
    print(-1)