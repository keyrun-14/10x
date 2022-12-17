# #prices = [7,1,5,3,6,4]
# n=int(input())
# price=[]
# for i in range(n):
#     price.append(int(input()))
# minm=float('inf')
# for j in range(n-1):
#     for k in range(j+1,n):
#         diff=price[j]-price[k]
#         if diff<minm:
#             minm=diff
#         else:
#             minm=minm

# if minm>=0:
#     print(0)
# else:
#     print(-minm)


#prices = [7,1,5,3,6,4]
# n=int(input())
# price=[]
# for i in range(n):
#     price.append(int(input()))
# minm=float('inf')
# for j in range(n-1):
#         if price[i]-<minm:
#             minm=diff
#         else:
#             minm=minm

# if minm>=0:
#     print(0)
# else:
#     print(-minm)




# n=input()
# print(chr(n))
# print(ord(n))
# for i in range(len(n)):
    # print(chr((ord(n[i])|(32))^32),end=" ")
    # print(chr((ord(n[i])|(32))),end=" ")

# def convert(list):
      
#     # Converting integer list to string list
#     s = [str(i) for i in list]
      
#     # Join list items using join()
#     res = int("".join(s))
      
#     return(res)

  
# # Driver code
# list = [1, 2, 3]
# print(convert(list))

n=int(input())
price=[]
for i in range(n):
    price.append(int(input()))
minm_price=float('inf')
profit=0
#prices = [7,1,5,3,6,4]
for i in range(n):
    if price[i]<minm_price:
        minm_price=price[i]
    elif price[i]-minm_price>profit:
        profit=price[i]-minm_price
print(profit)

