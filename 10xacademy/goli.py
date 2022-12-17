n=int(input())
for i in range(n):
    a,b,c=map(int,input().split())
    d=c-(a+b)
    print(abs(d))