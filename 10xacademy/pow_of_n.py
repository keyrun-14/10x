# n=int(input())
# while n>1:
#     n=n//4
# if n==1:
#     print(True)
# else:
#     print(False)
# for n in range(8,1025):
#     a=n&n-1
#     if a==0 and n//2&n//2-1==0:
#         print(n,"&",n-4," = ",a)
for i in range(10):
    print("4 ^",i," = ",4**i,end="||")
for i in range(10):
    n=4**i
    res=[]
    while n>0:
        a=n%2
        res.append(a)
        n=n//2
    
    reverse=res[::-1]
    print("4 ^",i," = ",4**i,"      ",reverse)