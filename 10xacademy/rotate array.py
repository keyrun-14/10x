# nums=list(map(int,input().split()))
# a=nums
# k=int(input())
# for i in range(k):
#     nums.insert(0,nums[-1])
#     nums.pop()
# print(nums)


# def rotate(nums,k):
#     print(nums[(len(nums)-k): ] + nums[:-k] )
# nums=list(map(int,input().split()))
# k=int(input())
# rotate(nums,k)

def sum_of_multiples(arr, N):
  res=0
  for i in arr:
    if i%N==0:
      res=i+res
  print(res)
if __name__=='__main__':
  list1=[]
  number=int(input())
  for i in list1:
    list1.split(',')
  (sum_of_multiples(list1, number))