n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
c=[]
m=int(input())
for j in range(m):    
    c=[]
    for i in range(0,int(len(a)/2)):
        b=a[i]+a[len(a)-i-1]
        c.append(b)
    if len(a)%2!=0:
        c.append(a[(len(a)//2)])    
    a=c
print(len(a))
print(*a,sep="\n")



# if m>1:
#         for i in range(0,(int(len(c)/2))):
#             e=c[i]+c[len(c)-i-1]
#             d.append(e)
#         if n%2!=0:
#             d.append(c[(len(c)//2)])
            
# if m==1:
#     print(len(c))
#     for i in range(len(c)):
#         print(c[i])
# elif m>1:
#     print(len(d))
#     for i in range(len(d)):
#         print(d[i])