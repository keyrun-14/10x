# a=[6,10,35,9,]
# maxx=-1*2**31
# for i in range(len(a)-1):
#     j=i  
#     k=2                                       
#     summ=0    
#     while k>0:     
#         summ=summ+a[j]  
#         j+=1
#         k-=1
#     if summ>maxx:     
#         maxx=summ    
# print(maxx)

# n= int(input())
# for i in range(n-1):
#     if i==0:
#         spaces=" "*(n-1)
#         stars="*"
#     else:
#         spaces=" "*((n-1)-i)
#         stars="*"+(" " * ((i*2)-1))+"*"
#     print(spaces+stars)
# for i in range(2*n-1):
#     print("*",end="")

n= int(input())
spaces=" "*(n-1)
stars="*"
print(spaces+stars)
for i in range(1,n-1):
    spaces=" "*((n-1)-i)
    stars="*"+(" " * ((i*2)-1))+"*"
    print(spaces+stars)
for i in range(2*n-1):
    print("*",end="")
