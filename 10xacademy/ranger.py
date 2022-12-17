# n=int(input())
# nums=list(map(int,input().split()))[:n]
# pro=1
# b=[]
# for i in range(n):
#     nums.append(nums[0])
#     nums.remove(nums[0])
#     a=nums[:n-1]
#     for j in a:
#         pro=pro*j
#     b.append(pro)
#     pro=1
# print(b)
def rangerproduct(nums,n):
    leftproduct=[1]*n
    # leftproduct[0]=1
    rightproduct=[1]*n
    # rightproduct[n-1]=1
    output=[1]*n
    for i in range(1,n):
        leftproduct[i]=leftproduct[i-1]*nums[i-1]
    for i in range(n-2,-1,-1):
        rightproduct[i]=rightproduct[i+1]*nums[i+1]
    for i in range(n):
        output[i]=leftproduct[i]*rightproduct[i]
    return output
no_of_testcases=int(input())
for i in range(no_of_testcases):
    n=int(input())
    nums=list(map(int,input().split()))[:n]
    print(*rangerproduct(nums,n))
