n=int(input())
a=[]
if -1000<n<1000:
    for i in range(n):
        b=int(input())
        a.append(b)
a.sort()
if 3<=len(a)<10**4:
    print(max(a[0]*a[1]*a[-1],a[-1]*a[-2]*a[-3]))