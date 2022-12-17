# def swaping(a,b):
#     a,b=b,a
#     # temp=a
#     # a=b
#     # b=temp
#     print(a,b)
# a=input()
# b=input()
# swaping(a,b)

# def ang(a,b):
#     # a=list(a)
#     # b=list(b)
#     d1={}
#     d2={}
#     for i in a:
#         if i not in d1:
#             d1[i]=1
#         else:
#             d1[i]+=1
#     for i in b:
#         if i not in d2:
#             d2[i]=1
#         else:
#             d2[i]+=1
#     if d1==d2:
#         return True
#     else:
#         return False
# a=input()
# b=input()
# print(ang(a,b))


# def summ(a,target):
#     arr=[]
#     for i in range(len(a)-1):
#         for j in range(1,len(a)):
#             if a[i]+a[j]==target:
#                 arr.append((a[i],a[j]))
#                 # print((a[i],a[j]))
#     return arr
# a=[1,2,3,4,5,6,7,8,9,10]
# target=10
# print(summ(a,target))

def summ(a,target):
    arr=[]
    d1={}
    for i in range(len(a)):
        d1[i]=i
    for key,value in d1.items():
        if target-key in d1:
            arr.append((key,target-key))
    return arr
a=[1,2,3,4,5,6,7,8,9,10]
target=10
print(summ(a,target))
