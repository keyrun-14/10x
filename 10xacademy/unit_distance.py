# from collections import Counter
# n=int(input())
# for i in range(n):
#     a,b=input().split()
#     d1=Counter(a)
#     d2=Counter(b)
#     if d1==d2:
#         print(False)    
#     elif d1!=d2:
#         count=0
#         for i in a:
#             if i not in d2:
#                 count+=1
#         if count==1:
#             print(True)
#         else:
#             print(False)
#     elif len(a)>len(b):
#         count1=0
#         for key , value in d2.items():
#             if d1[key]<d2[key] or d1[key]<d2[key]:
#                 diff=abs(d1[key]-d2[key])
#                 if diff==1:
#                     print(True)
#                 else:
#                     print(False)
def unit_distance(str1,str2):
    if str1==str2:
        return False
    diff=len(str1)-len(str2)
    i=0
    j=0
    count=0
    while i<len(str1) and j<len(str2):
        if str1[i]==str2[j]:
            i+=1
            j+=1
        else:
            count+=1
            if diff == 0:
                i=i+1
                j=j+1
            elif diff == -1:
                j+=1
            elif diff==1:
                i+=1
            if count>1:
                return False    
    if i<len(str1) or j<len(str2):
        count=count+1
    return count==1
for i in range(int(input())):
    str1,str2=input().split()
    print(unit_distance(str1,str2))