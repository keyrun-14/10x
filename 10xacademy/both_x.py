
import collections


# for i in range(int(input())):
#     a,b,c=input().split()
#     a,b,c=str(a),str(b),int(c)
#     d=defaultdict(int)
#     for i in range(len(a)):
#         if a.count(a[i])==c:
#             d.append(a[i])
#     e=[]
#     for i in d:
#         if i in b and b.count(i)==c:
#             e.append(i)
#     e.sort()
#     print(*e)

for i in range(int(input())):
    a,b,c=input().split()
    a,b,c=str(a),str(b),int(c)

    d={}
    for i in a:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    e={}
    for i in b:
        if i in e:
            e[i]+=1
        else:
            e[i]=1

    for i in d:
        if d[i] == c:
            
            print(i,d[i])

# ggekf ggffmn 2

# g

# d = {}

# s = ggekf
# g -> 2
# e -> 1
# k -> 1
# f -> 1

# s = ggffmn

# #d[key] = min(d[key], s.count(key))
# for key in d:
# 	if d[key] != s.count(key) :
# 		d[key] = 0


# g->2
# e->0
# k->0
# f->0

# res = []

# for key in d:
# 	# if key > 0:
# 	if d[key] == x:
# 		res.append(key)

# res.sort()
# Group discussion 2|10x Academy|
    

# ggekff ggffmn 2

# f g

# d1 = {}
# d2 = {}

# s1 = ggekff
# s2 = ggffmn

# d1:
# g -> 2
# e -> 1
# k -> 1
# f -> 2

# d2:
# g->2
# f->2
# m->1
# n->1

# res = []

# for key in d1:
# 	if d1[key] == x and d1[key] == d2[key]:
# 		res.append(key)

# res.sort()
# print(res)
# time complexity: O(n) + O(k logk)