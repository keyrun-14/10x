# def sort(a):
#     left=[]
#     right=[]
#     if len(a)<=1:
#         return a
#     else:
#         pivot=a.pop(len(a)//2)
#     for i in a:
#         if i<=pivot:
#             left.append(i)
#         else:
#             right.append(i)
#     return sort(left)+[pivot]+sort(right)
# a=[0,0,1,1,1,0,1,0,0,1,1,1,1,0]
# print(sort(a))
a=[0,0,1,1,1,0,1,0,0,1,1,1,1,0]
length=len(a)
i=len(a)-1
j=len(a)-2

while length:
    if a[i]<a[j]:
        a[i],a[j]=a[j],a[i]
        i=i-1
        # j=j-1
    if i==j:
        
        j=j-1
    if i>j:
        i=i-1
        # j=j-1
    length=length-1
print(a)
    

