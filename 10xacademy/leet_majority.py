nums=list(map(int,input().split()))
nums.sort()
set1=set()
last=0
count=1
if len(nums)==1:
    print(nums)
else:
    print(nums)
    for i in range(len(nums)-1):
        if nums[i]==nums[i+1]:
            count+=1            
        elif count > len(nums)/3:
            set1.add(nums[i])
            count=1
        else:
            count=1            
        last=nums[i+1]        
    if count > len(nums)/3:
        set1.add(last)
    print(*list(set1))
    # 4 1 3 1 3 3 1 2 3 2 4 2 1 4 4 4 4 4