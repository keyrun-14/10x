# a=list(map(int,input()))
# for i in range(len(a)):
#     rem=a[i]%10
#     b=rem+1
#     map(int,str(b))
#     a[len(a)-1]=b 
# print(a)

a=list(map(int,input()))
#a=int(input())
b=str(a)
c=a+1
d=list(map(int,str(c)))
print(d)