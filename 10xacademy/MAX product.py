x=int(input())
y=int(input())
a=list(map(int,input().split()))[:x]
b=list(map(int,input().split()))[:y]
c,d=0,0

if abs(min(a))>abs(max(a)):
    c=min(a)
else:
    c=max(a)
if abs(min(b))>abs(max(b)):
    d=min(b)
else:
    d=max(b)
print(abs(c*d))








# x=int(input())
# y=int(input())
# a=list(map(int,input().split()))[:x]
# b=list(map(int,input().split()))[:y]
# a.sort()
# b.sort()
# c,d=0,0
# if abs(a[0])>abs(a[-1]):
#     c=a[0]
# else:
#     c=a[-1]
# if abs(b[0])>abs(b[-1]):
#     d=b[0]
# else:
#     d=b[-1]
# print(abs(c*d))




# x=int(input())
# y=int(input())
# a=list(map(int,input().split()))[:x]
# b=list(map(int,input().split()))[:y]
# for i in a:
#     for j in b:
#         c=abs(i)*abs(j)
#         d.append(c)
# print(max(d))

