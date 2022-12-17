def smally(n,arr):
    d={}
    arr_temp=sorted(arr)
    for i in range(len(arr)):
        if arr_temp[i] not in d:
            d[arr_temp[i]]=i

    for i in range(len(arr)):
        print(d[arr[i]])

n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
smally(n,arr)






# noofdigits = int(input())
# nums = [int(input()) for i in range(noofdigits)]
# sornums = sorted(nums, reverse=True)
# dictcount = {}
# for i in range(noofdigits-1):
#     if sornums[i] != sornums[i+1]:
#         dictcount[sornums[i]] = noofdigits-1-i
# dictcount[sornums[-1]] = 0
# for i in nums:
#     print(dictcount[i])



# nums = [8,1,2,2,3]

# cnt =[0 1 2 1 0 0 0 0 1 0 0 ... 100] -- O(n)
# idx = 0 1 2 3 4 5 6 7 8 9 10 ... 100

# sum =[0 1 3 4 4 4 4 4 5 5 5 ...   5]
# idx = 0 1 2 3 4 5 6 7 8 9 10 ... 100

# nums= [8,1,2,2,3]
# res = [4,0,1,1,3]

# Time Complexity: O(n)

# cnt=[] -- 101 -- 0
# traverse nums array -- for loop -- i (8 to 3)
# 	cnt[i]+=1;
# get cnt array

# sum[i] = cnt[i]+sum[i-1];

# res[i] = sum[nums[i-1]];


# HASH MAP :-

# size -- 5
# nums = [8,1,2,2,3]
# sorted = [8,3,2,2,1] -- (nums.sort, reverse = true)

# dictcnt = {}
# loop
# 	if sorted[i] != sorted[i+1]
# 	8 -> size - i - 1; i=0 -- 4
# 	3 -> size - i - 1; i=1 -- 3
# 	2 -> size - i - 1; i=3 -- 1
# 	1 -> size - i - 1; i=4 -- 0
# Time Complexity : O(nlogn)
# Abhishek Ranjan2:11 PM
# space complexity : O(n) -- constant(if we print it directly)

# counting sort -- TC O(n+k) .. SC O(k)



# from collections import Counter
# def smally(n,arr):
#     d=Counter(arr)
#     s=0
#     print(sorted(d.keys()))
#     for i in sorted(d.keys()):
#         print(d[i])
#         d[i],s=s,s+d[i]
#     for i in arr:
#         print(d[i])

# n=int(input())
# arr=[]
# for i in range(n):
#     arr.append(int(input()))
# smally(n,arr)
