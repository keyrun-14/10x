# for _ in range(int(input())):
#     n = int(input())
#     arr = [int(x) for x in input().split()]
#     arr2 = sorted(arr)
#     count = 0
#     for i in range(n):
#         k = abs(i - arr.index(arr2[i]))
#         if k%2!=0:
#             count += 1
#     print(count//2)

for _ in range(int(input())):
    n = int(input())
    arr = [int(x) for x in input().split()]
    arr2 = sorted(arr)
    arr_set=set()
    sorted_arr_set=set()
    for i in range(0,len(arr),2):
        arr_set.add(arr[i])
        sorted_arr_set.add(arr2[i])
    diff=arr_set-sorted_arr_set
    print(len(diff))

