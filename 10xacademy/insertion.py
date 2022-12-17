# def insert(arr,n):
#     # Your code goes here
#     for i in range(1,n):
#         current=arr[i]
#         previous=i-1
#         while previous>=0 and current<arr[previous]:
#             arr[previous+1]=arr[previous]
#             previous-=1
#         arr[previous+1]=current
#     return arr

# ### DO NOT EDIT ANYTHING BELOW THIS LINE

# if __name__=='__main__':
#     n = int(input())
#     arr = [int(x) for x in input().split()]
#     insert(arr, n)
#     print(*arr)

#Insertion sort
ar = [5,4,3,2,1]

for i in range(1, len(ar)):
    while ar[i-1] > ar[i] and i > 0:
        ar[i-1], ar[i] = ar[i], ar[i-1]
        i -= 1
        print(ar)