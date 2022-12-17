# a=[4]
# count=0
# minn=-999999999999#3#5#6
# k=0
# j=1
# while len(a)>1:
#     count=sum([a[k]:a[j+1]])
#     if count>minn:
#         minn=count
#         j+=1
#     else:
#         minn=minn
#         k+=1
#         a=a[a[k]:]   
#         k=0
#         j=1
# ifa[0]>minn:
#     minn=a[0]
# else:
#     print(minn)

# -2+1=-1>minn     #-1
# -1-3=-4<minn=-1  -1
# 1-3=-2<-1
# -3+4=1>minn=>minn=1
# 1+-1=0<minn=>minn=1

# def segregate0and1(arr, size):
#     # Initialize left and right indexes
#     left, right = 0, size-1
     
#     while left < right:
#         # Increment left index while we see 0 at left
#         while arr[left] == 0 and left < right:
#             left += 1
 
#         # Decrement right index while we see 1 at right
#         while arr[right] == 1 and left < right:
#             right -= 1
 
#         # If left is smaller than right then there is a 1 at left
#         # and a 0 at right. Exchange arr[left] and arr[right]
#         if left < right:
#             arr[left] = 0
#             arr[right] = 1
#             left += 1
#             right -= 1
 
#     return arr
 
# # driver program to test
# arr = [0, 1, 0, 1, 1, 1]
# arr_size = len(arr)
# print("Array after segregation")
# print(segregate0and1(arr, arr_size))

# def segregate0and1(arr, size):
 
#     type0 = 0
#     type1 = size - 1
     
#     while(type0 < type1):
#         if(arr[type0] == 1):
#             (arr[type0],arr[type1]) = (arr[type1],arr[type0])
#             type1 -= 1
#         else:
#             type0 += 1
     
# # Driver Code
# arr = [0, 1, 0, 1, 1, 1]
# arr_size = len(arr)
# segregate0and1(arr, arr_size)
# print("Array after segregation is",
#                          end = " ")
# for i in range(0, arr_size):
#         print(arr[i], end = " ")





