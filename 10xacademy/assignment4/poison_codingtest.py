t=int(input())
if t>0:
    for i in range(t):
        n=int(input())
        if n>0:
            a=list(map(int,input().split()))[:n]
            strength=0
            for k in range(len(a)):
                if a[k]>0:
                    strength=strength+a[k]
            while strength>1:
                strength=strength/2
            if strength==1:
                print("Yes")
            else:
                print("No")
