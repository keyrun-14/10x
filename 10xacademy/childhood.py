# from collections import Counter
# for i in range(int(input())):
#     a,b=input().split()
#     s=input()
#     count1=Counter(s)
#     dummy_string = ""
#     for i in s:
#         if i== a:
#             count1[a]=b
#             dummy_string += count1[i]
#         elif i== b:
#             count1[b]=a
#             dummy_string += count1[i]
#         else:
#             count1[i]=i
#             dummy_string += count1[i]
#     print(dummy_string)

d={}
for i in range(int(input())):
    a,b=input().split()
    d[a]=b
    d[b]=a
s=input()
dummy_string = ""
for i in s:
    if i in d:
        dummy_string += d[i]
    else:
        dummy_string += i
print(dummy_string)