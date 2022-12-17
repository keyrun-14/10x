N=int(input())
n=[]
if N%2!=0:
    for i in range(N):
        n.append(int(input()))
    for i in n:
        a=n.count(i)
        if a==1:
            print(i)
