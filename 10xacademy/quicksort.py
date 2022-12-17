# def quicksort(arr):
#     left = []
#     right = []
#     if len(arr) < 1:
#         return arr
#     pivot = arr.pop(arr[0])
#     for i in range(len(arr)):
#         if arr[i] <= pivot:
#             left.append(arr[i])
#         else:
#             right.append(arr[i])
#     return quicksort(left)+[pivot]+quicksort(right)   
# n=int(input())
# arr = list(map(int, input().split()))
# print(*quicksort(arr))

from collections import Counter
d1 = {'key1': 50, 'key2': 100, 'key3':200}
d2 = {'key1': 200, 'key2': 100, 'key4':300}
new_dict = Counter(d1) + Counter(d2)
print(new_dict)