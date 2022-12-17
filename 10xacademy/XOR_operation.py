n=int(input())
start=int(input())
nums=[]
for i in range(n):
    nums.append(start+ 2*i)
if n==1:
    print(nums[0])
else:
    x=nums[0]^nums[1]
    for i in range(2,n):
        x=x^nums[i]
    print(x)




# def XOR(nums):
#     if n==5:
#         return 
#     n+=1
#     return nums[n] ^ XOR(nums[n+1])
# nums=[0,2,4,6,8]
# n=0
# print(XOR(nums))