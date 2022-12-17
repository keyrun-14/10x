def special_bit():
    for i in range(Q):
        start,end=map(int,input().split())
        count2=0      
        for i in arr[start-1:end]:
            count=0
            while i>0:
                a=i&1
                if a==1:
                    count+=1               
                else:
                    count=0
                i>>=1
                if count==2:
                    count2+=1
                    break        
        print(count2)
        count2=0     
N,Q=map(int,input().split())
arr=list(map(int,input().split()))[:N]
special_bit()