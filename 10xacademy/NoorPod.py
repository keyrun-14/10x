# for i in range(int(input())):
#     n=int(input())
#     arr=[]
#     Eset=set()
#     Sset=set()
#     for i in range(n):
#         s,e=map(int,input().split())
#         arr.append([s,e])
#         Eset.add(e)
#         Sset.add(s)
#     print(Eset)
#     print(Sset)
#     arr1=arr[::-1]
#     print(arr)
#     # arr1.sort()
#     print(arr1)
#     set_diff=Eset-Sset
#     print(set_diff)


for i in range(int(input())):
    n=int(input())
    arr=[]
    Eset=set()
    Sset=set()
    for i in range(n):
        s,e=map(int,input().split())
        arr.append([s,e])
        Eset.add(e)
        Sset.add(s)
    print(Eset)
    print(Sset)
    arr2=[]
    for i in arr:
        arr2.append(i[::-1])
    print(arr)
    # arr1.sort()
    print(arr2)
    set_diff=Eset-Sset
    print(set_diff)

# 1
# 3
# 4 1
# 5 4
# 7 3