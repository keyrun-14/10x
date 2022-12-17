def mergetwolists(a,b):
   
    for i in range(len(b)):
        a.append(b[i])
    a.sort()
    print(a)
a=list(map(int,input().split()))
b=list(map(int,input().split()))

mergetwolists(a,b)