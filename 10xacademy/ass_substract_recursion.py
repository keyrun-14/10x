
# your code goes here
def addSub(arr, x, n, i, summ, count):
    #base case
    if i == n:
        if summ == x:
            count.append(1)
        return
    addSub(arr, x, n, i+1, summ+arr[i], count)
    addSub(arr, x, n, i+1, summ-arr[i], count)
    addSub(arr, x, n, i+1, summ, count)
target=int(input())
n=int(input())
arr=[int(x) for x in input().split()]
count=[]
addSub(arr, target, n, 0, 0, count)
print(sum(count)) #addsubtract