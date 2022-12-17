# n,k=input().split()
# n,k=int(n),int(k)
# arr=list(map(int,input().split()))[:n]
# d=[]
# sum=0
# count=0
# for i in range(len(arr)-1):
#     for j in range(i,len(arr)):
#         sum=sum+arr[j]
#         count+=1
#         if sum==k:
#             d.append(count)
#             count=0
# print(d)

n,k=input().split()
n,k=int(n),int(k)
arr=list(map(int,input().split()))[:n]
d=[]
sum=0
count=0
for i in range(len(arr)):

        sum=sum+arr[j]
        count+=1
        if sum==k:
            d.append(count)
            count=0
print(d)
            
        
# # Python3 implementation to find the length
# # of longest subArray having sum k
 
# # function to find the longest
# # subarray having sum k
# def lenOfLongSubarr(arr, n, k):
 
#     # dictionary mydict implemented
#     # as hash map
#     mydict = dict()
 
#     # Initialize sum and maxLen with 0
#     sum = 0
#     maxLen = 0
 
#     # traverse the given array
#     for i in range(n):
 
#         # accumulate the sum
#         sum += arr[i]
 
#         # when subArray starts from index '0'
#         if (sum == k):
#             maxLen = i + 1
 
#         # check if 'sum-k' is present in
#         # mydict or not
#         elif (sum - k) in mydict:
#             maxLen = max(maxLen, i - mydict[sum - k])
 
#         # if sum is not present in dictionary
#         # push it in the dictionary with its index
#         if sum not in mydict:
#             mydict[sum] = i
 
#     return maxLen
 
# # Driver Code
# if __name__ == '__main__':
#     arr = [10, 5, 2, 7, 1, 9]
#     n = len(arr)
#     k = 15
#     print("Length =", lenOfLongSubarr(arr, n, k))