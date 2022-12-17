a,b=map(int,input().split())
for i in range(b):
    c=int(input())
    if c==1:
        print(0)
    if c==2:
        print(1)
    if c==3:
        print(2)

    if c>3:
        count=2
        for i in range(1,c//6+1):
            if 6*i+1<=a:
                count+=1
            if  6*i-1<=a:
                count+=1
        print(count)
