# from collections import Counter
# for i in range(int(input())):
#     s,t=input().split()
#     d1=Counter(s)
#     d2=Counter(t)
#     if d1==d2:
#         print(True)
#     else:
#         print(False)

for i in range(int(input())):
    s,t=input().split()
    s=sorted(s)
    t=sorted(t)
    if s==t:
        print(True)
    else:
        print(False)