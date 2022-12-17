# def string_repeat(s,n):
    
#     for i in range(n-1):
#         r=s+" "
#         print(r,end="")
#     print(s,end=" ")
# s=input()
# n=int(input())
# (string_repeat(s,n))

def string_repeat(s,n):    
    res=s*n
    print(*res)
s=str(input()).split()
n=int(input())
(string_repeat(s,n))
