nums=list(map(int,input().split()))
nums1=set(nums)
num2=list(nums1)
print(num2)
if len(num2)<3:
    print(max(num2))
else:
    print(num2[0])