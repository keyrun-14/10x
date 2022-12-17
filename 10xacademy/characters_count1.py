# a=list(map(str,input().split()))
# d={}
# for i in a:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)
# for key,value in d.items():
#     print(key+str(value),end="")
# a a a a a b b b b d d d d d c c c c a a a a

# a=list(map(str,input().split()))
# count=1
# d=[]
# x=""
# for i in range(len(a)-1):
#     if a[i]==a[i+1]:
#         count=count+1        
#     else:
#         d.append(a[i])        
#         d.append(count)
#         count=1
#     x=a[i+1]
#     count=count
# d.append(x)
# d.append(count)
# print(d)
# for i in d:
#     print(str(i),end="")

#a a a a a g g g g h h h h h b b b b b a b c d
lst=list(input().split())
lst.sort()
res=''
count=1
finalStr=''
for i in range(len(lst)-1):
    if lst[i]==lst[i+1]:
        count=count+1
    else:
        finalStr=finalStr+res+str(count)
        count=1
    res=lst[i+1]
    count=count
finalStr=finalStr+res+str(count)
print(finalStr)

# a=list(map(str,input().split()))
# count=1
# d=""
# x=""
# for i in range(len(a)-1):
#     if a[i]==a[i+1]:
#         count=count+1
#         x=a[i]
#     else:
#         d=d+x+str(count)       
#         count=1
# d=d+x+str(count)

# print(d)
# for i in d:
#     print(str(i),end="")

# lst=list(input().split())
# res=''
# count=1
# finalStr=''
# for i in range(len(lst)-1):
#     if lst[i]==lst[i+1]:
#         res=lst[i]
#         count=count+1
#     else:
#         if count>1:
#             finalStr=finalStr+res+str(count)
#             count=1
#         else:
#             finalStr=finalStr+lst[i]+str(count)
#             if i==len(lst)-2:
#                 res=lst[i+1]
#                 count=1
# finalStr=finalStr+res+str(count)
# print(finalStr)