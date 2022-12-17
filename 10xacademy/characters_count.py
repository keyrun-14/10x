a=list(map(str,input().split()))
d={}
for i in a:
    if i in d:
        d[i]+=d[i]+1
    else:
        d[i]=1
print(d)
# a a a a a b b b b d d d d d c c c c a a a a