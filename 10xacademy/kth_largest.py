nums=list(map(int,input().split()))
k=int(input())
nums.sort()
l=len(nums)
print(nums[l-k])