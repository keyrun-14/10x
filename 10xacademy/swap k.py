N,K=input().split()
N,K=int(N),int(K)
Arr=list(map(int,input().split()))[:N]
Arr[K-1],Arr[len(Arr)-K]=Arr[len(Arr)-K],Arr[K-1]
print(Arr)