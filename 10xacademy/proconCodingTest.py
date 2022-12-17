def mergesort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        l=arr[:mid]
        r=arr[mid:]
        mergesort(l)
        mergesort(r)
        i=j=k=0
        while i <len(l)  and j<len(r):
            if l[i]<r[j]:
                arr[k]=l[i]
                i+=1
            else:
                arr[k]=r[j]
                j+=1
            k+=1
        while i <len(l):
            arr[k]=l[i]
            i+=1
            k+=1
        while j<len(r):
            arr[k]=r[j]
            j+=1
            k+=1
for i in range(int(input())):
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(list(map(int,input().split())))
    arr2=[]
    for i in arr:
        arr2.append(i[::-1])
    mergesort(arr)
    mergesort(arr2)
    arr2=arr2[::-1]
    favor1=arr[n-1][0]+arr[n-2][0]
    anger1=0
    for i in range(n-2):
        anger1+=arr[i][1]
    beauty1=(favor1-anger1)

    favor2=arr2[0][1]+arr2[1][1]
    anger2=0
    for i in range(2,n):
        anger2+=arr2[i][0]
    beauty2=(favor2-anger2)
    if beauty1>beauty2:
        print(beauty1)
    else:
        print(beauty2)
# arr=[[2, 3], [10, 2], [11, 5], [4, 1]]
# arr.sort()
# print(arr)
# arr2=[]
# for i in arr:
#     arr2.append(i[::-1])
# arr2.sort()
# print(arr2)
# for i in range(int(input())):
#     n = int(input())
#     arr = []
#     for i in range(n):
#         arr.append(list(map(int, input().split())))
#     arr.sort()
#     favor = arr[n-1][0]+arr[n-2][0]
#     anger = 0
#     for i in range(n-2):
#         anger += arr[i][1]
#     print(favor-anger)

# 1
# 4
# 2 3
# 10 2
# 11 5
# 4 1
