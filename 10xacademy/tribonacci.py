N=int(input())
a=[0,0,1]
if N==0:
    print(0)
elif N==1:
    print(0)
elif N==2:
    print(1)
else:
    for i in range(N-3):
        b=sum(a[i:])
        a.append(b)
        
        print(b)
        print(a)