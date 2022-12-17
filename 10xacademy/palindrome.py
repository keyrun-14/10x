# # n=int(input())
# # sum=0
# # k=n
# # while n>0:
# #     reverse=n%10
# #     sum=sum*10+reverse
# #     n=n//10
# # #print(sum)
# # if k==sum:
# #     print(True)
# # else:
# #     print(False)


# #check if given string/number is palindrome or not 
# # def checkPalindrome(str):     
# # Run loop from 0 to len/2    
# # for i in range(0, len(str)//2):       
# # if str[i] != str[len(str)-i-1]:           
# # return False  
# # If the above loop doesn't  
# # return then it is palindrome    
# # return True

# def checkPalindrome(str):
#     for i in range(len(str)//2):
#         if str[i] != str[len(str)-i-1]:
#             return False
#     return True
# s=input()
# print(checkPalindrome(s))

# n=int(input())
# x=int(input())
# parent=list(map(int,input().split()))[:n]
# sub=[0]*n
# c=0
# for i in range(n):
#     if parent[i] != -1:
#         sub[parent[i]]+=1
# for j in range(n):
#     if sub[j]>=x:
#         c=c+1
# print(c)

n=input1
x=input2
parent=input3
sub=[0]*n
c=0
for i in range(n):
    if parent[i] != -1:
        sub[parent[i]]+=1
for j in range(n):
    if sub[j]>=x:
        c=c+1
return c

