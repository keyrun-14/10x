def colorsort(n,array_nums):

    color_sort=[]

    for i in range(n):
        if array_nums[i]==0:
            color_sort.append(array_nums[i])
    for i in range(n):
        if array_nums[i]==1:
            color_sort.append(1)
    for i in range(n):
        if array_nums[i]==2:
            color_sort.append(2)

    print(*color_sort,sep="\n")
n=int(input())
array_nums=[]

for i in range(n):
    array_nums.append(int(input()))

colorsort(n,array_nums)