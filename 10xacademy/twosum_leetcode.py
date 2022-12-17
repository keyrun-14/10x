def twosum(nums,target):
    a=[]
    for i in range(len(nums)-1):
        if target==nums[i]+nums[i+1]:
            a.append(i)
            a.append(i+1)
    print(a)
nums=list(map(int,input().split()))
target=int(input())
twosum(nums,target)