# n=int(input())
n=5
# arr=list(map(int,input().split()))[:n]
arr=[21,71,34,1,0]
# arr=[7,3,4,8,9]
arr2=sorted(arr)
print(arr)
print(arr2)
count=0
for i in range(n-1):
    for j in range(i+1,n):
        if arr[i]<=arr[j]:
            count+=1
print(count)
count1=0
for i in range(len(arr)):
    if arr[i]==arr2[i]:
        count1+=1
print(count1)



# # # n=int(input())
# # # arr=list(map(int,input().split()))[:n]
# # # count=0
# # # i=0
# # # j=1
# # # while i<j:
# # #     if arr[i]<=arr[j]:
# # #         count+=1
# # #         print(arr[i],"  ",arr[j])
# # #         j-=1
# # #     else:
# # #         i+=1
# # #         j=i+1
# # # print(count)

# # # from collections import Counter


# # # n=int(input())
# # # arr=list(map(int,input().split()))[:n]
# # # count=0
# # # i=0
# # # j=1
# # # dict=Counter(arr)
# # # dict2={}
# # # for i in range(len(arr)):
# # #     dict2[arr[i]]=i
# # # print(dict)
# # # print(dict2)
# # # for key, value in dict.items():
# # #     if 
# # # print(count)
# # # arr=[1,2,3,4]
# # # k=2
# # # print(k>arr)

# # # arr=[3,2,1,3,5]
# # # arr2=sorted(arr)
# # # print(arr)
# # # print(arr2)

# # ##[3, 2, 1, 3, 5]
# # ##[1, 2, 3, 3, 5]
# # ## 3
# # ## soterd arr pairs =10


# # Python 3 program to count inversions in an array

# # Function to Use Inversion Count


# # def mergeSort(arr, n):
# # 	temp_arr = [0]*n
# # 	return _mergeSort(arr, temp_arr, 0, n-1)
# # def _mergeSort(arr, temp_arr, left, right):
# # 	inv_count = 0
# # 	if left < right:
# # 		mid = (left + right)//2
# # 		inv_count += _mergeSort(arr, temp_arr,left, mid)
# # 		inv_count += _mergeSort(arr, temp_arr,mid + 1, right)
# # 		inv_count += merge(arr, temp_arr, left, mid, right)
# # 	return inv_count
# # def merge(arr, temp_arr, left, mid, right):
# # 	i = left	
# # 	j = mid + 1 
# # 	k = left	 
# # 	inv_count = 0
# # 	while i <= mid and j <= right:
# # 		if arr[i] <= arr[j]:
# # 			temp_arr[k] = arr[i]
# #             inv_count+= (mid-i+1)
# #             k += 1
# # 			i += 1
# # 		else:
# # 			temp_arr[k] = arr[j]
# # 			k += 1
# # 			j += 1
# # 	while i <= mid:
# # 		temp_arr[k] = arr[i]
# # 		k += 1
# # 		i += 1
# # 	while j <= right:
# # 		temp_arr[k] = arr[j]
# # 		k += 1
# # 		j += 1
# # 	for loop_var in range(left, right + 1):
# # 		arr[loop_var] = temp_arr[loop_var]
# # 	return inv_count
# # arr = [1, 20, 6, 4, 5]
# # n = len(arr)
# # result = mergeSort(arr, n)
# # print("Number of inversions are", result)








# # Python 3 program to count inversions in an array

# # Function to Use Inversion Count


# def mergeSort(arr, n):
# 	# A temp_arr is created to store
# 	# sorted array in merge function
# 	temp_arr = [0]*n
# 	return _mergeSort(arr, temp_arr, 0, n-1)

# # This Function will use MergeSort to count inversions


# def _mergeSort(arr, temp_arr, left, right):

# 	# A variable inv_count is used to store
# 	# inversion counts in each recursive call

# 	inv_count = 0

# 	# We will make a recursive call if and only if
# 	# we have more than one elements

# 	if left < right:

# 		# mid is calculated to divide the array into two subarrays
# 		# Floor division is must in case of python

# 		mid = (left + right)//2

# 		# It will calculate inversion
# 		# counts in the left subarray

# 		inv_count += _mergeSort(arr, temp_arr,
# 								left, mid)

# 		# It will calculate inversion
# 		# counts in right subarray

# 		inv_count += _mergeSort(arr, temp_arr,
# 								mid + 1, right)

# 		# It will merge two subarrays in
# 		# a sorted subarray

# 		inv_count += merge(arr, temp_arr, left, mid, right)
# 	return inv_count

# # This function will merge two subarrays
# # in a single sorted subarray


# def merge(arr, temp_arr, left, mid, right):
# 	i = left	 # Starting index of left subarray
# 	j = mid + 1 # Starting index of right subarray
# 	k = left	 # Starting index of to be sorted subarray
# 	inv_count = 0

# 	# Conditions are checked to make sure that
# 	# i and j don't exceed their
# 	# subarray limits.

# 	while i <= mid and j <= right:

# 		# There will be no inversion if arr[i] <= arr[j]

# 		if arr[i] <= arr[j]:
# 			temp_arr[k] = arr[i]
# 			k += 1
# 			i += 1
# 		else:
# 			# Inversion will occur.
# 			temp_arr[k] = arr[j]
# 			inv_count += (mid-i + 1)
# 			k += 1
# 			j += 1

# 	# Copy the remaining elements of left
# 	# subarray into temporary array
# 	while i <= mid:
# 		temp_arr[k] = arr[i]
# 		k += 1
# 		i += 1

# 	# Copy the remaining elements of right
# 	# subarray into temporary array
# 	while j <= right:
# 		temp_arr[k] = arr[j]
# 		k += 1
# 		j += 1

# 	# Copy the sorted subarray into Original array
# 	for loop_var in range(left, right + 1):
# 		arr[loop_var] = temp_arr[loop_var]

# 	return inv_count


# # Driver Code
# # Given array is
# arr = [1, 20, 6, 4, 5]
# n = len(arr)
# result = mergeSort(arr, n)
# print("Number of inversions are", result)

# # This code is contributed by ankush_953
