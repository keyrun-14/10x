# from collections import Counter
# for i in range(int(input())):
#     name,tyed_name=input().split()
#     d1=Counter(name)
#     d2=Counter(tyed_name)
#     flag=False
#     for key,value in d1.items():
#         if d1[key]<=d2[key]:
#             flag=True
#         else:           
#             flag=False
#             break    
#     print(flag)

for i in range(int(input())):
    name,tyed_name=input().split()
    count=0
    for i in range(len(name)):
        j=0
        while name[i]==tyed_name[j]:
            count=count+1
            j+=1
        