def recursive_print(l,r):
    if l>=r:
        print(r)
        return
    print(l,end=" ")
    recursive_print(l+1,r)
    return 
for i in range(int(input())):
    l,r=map(int,input().split())
    (recursive_print(l,r))


