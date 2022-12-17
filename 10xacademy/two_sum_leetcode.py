# a=[2,4,11,3]
# a=[3,3]
# b=6
# for i in range(len(a)-1,-1,-1):
    
#     if b-a[i] in a[:i]:
#         end_index=i
#         print(end_index)
#         c=a[i]
#         print(c)
#         break
# for i in range(len(a)):
#     if c+a[i]==b:
#         start_index=i
#         break
# print([start_index,end_index])
a=[1,2,4,7,10]
b=9
print(a[:4])
d={}
for i in range(len(a)):
    d[a[i]] = i
    print(d)
    print()
print(d[7])

for i in range(len(a)):
    print(b-a[i],b,a[i])

    if b-a[i] in d:
        print(i, d[b-a[i]])
        break