n=int(input())
a=[1]
c=[1,1]
if n==1:
    print(1)
elif n==2:
    print(c)
else:
    while (n-2)>0:           
        for i in range(1,len(c)):
            b=c[i-1]+c[i]
            a.append(b)    
        a.append(1)
        c=a
        a=[1]
        n=n-1
    print(*c,sep="\n")