t=int(input())

for i in range(t):
    n=int(input())
    if n<=0:
        print(-1)
    
    elif n==1:
        print(1)

    else:
        b=list(map(int,input().split()))[:n]    

        if b[0]>b[1] :
            print(1)
        
        elif b.count(b[0])==len(b):
                print(-1)
        
        elif n>2:
            for i in range(1,n-2):
                
                if (b[i]<b[i+1]>b[i+2] and b[n-2]<b[n-1]) or (b[i]<b[i+1]>b[i+2] and b[n-2]>b[n-1]):
                    print(i+2)
                    break
                
            else:
                if (b[n-1]>b[n-2] and b[i]<b[i+1]<b[i+2]) or (b[n-1]>b[n-2] and b[i]==b[n-2]):
                    print(n)
                else:
                    print(-1)