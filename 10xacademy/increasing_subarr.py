n=int(input())
arr=list(map(int,input().split()))
MaxLen = 1
CurLen = 1
StartingIndex = 0
for i in range(1,n):
    if (arr[i] > arr[i-1]):
        CurLen = CurLen + 1
    else :
        if (MaxLen < CurLen):
            MaxLen = CurLen
            StartingIndex = i - MaxLen
        CurLen = 1 
if (MaxLen < CurLen):
    MaxLen = CurLen
    StartingIndex = n - MaxLen
print(MaxLen , StartingIndex + 1 , MaxLen + StartingIndex , end=" ")


# def IncreasingSubarr(arr,n):
# 	MaxLen = 1
# 	CurLen = 1
# 	StartingIndex = 0
# 	for i in range(1,n):
# 		if (arr[i] > arr[i-1]):
# 			CurLen = CurLen + 1
# 		else :
# 			if (MaxLen < CurLen):
# 				MaxLen = CurLen
# 				StartingIndex = i - MaxLen
# 			CurLen = 1 
# 	if (MaxLen < CurLen):
# 		MaxLen = CurLen
# 		StartingIndex = n - MaxLen
# 	print(MaxLen , StartingIndex + 1 , MaxLen + StartingIndex , end=" ")
# n = int(input())
# arr = [int(x) for x in input().split()]
# IncreasingSubarr(arr, n)