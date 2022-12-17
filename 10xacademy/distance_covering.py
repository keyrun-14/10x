# def distance_covering(n,count):
   
#     if n==1 or n==0:
#         return n
    
#     return distance_covering(n-1,count-1)
# n=int(input())
# count=0
# print(distance_covering(n,count))

# def distance_covering(n):
#     if n < 0:
#         return 0
#     if n==0:
#         return 1
    
#     return distance_covering(n-1)+distance_covering(n-2)
# t=int(input())
# for i in range(t):
#     n=int(input())
#     print(distance_covering(n))

def distance_covering(n):

    if n==0 or n==1:
        return 1
    
    return distance_covering(n-1)+distance_covering(n-2)
t=int(input())
for i in range(t):
    n=int(input())
    print(distance_covering(n))

    # #6
    #             13 ways


    # #5
    # 1 1 1 1 1 
    # 1 1 1 2
    # 1 1 2 1
    # 1 2 1 1
    # 2 1 1 1
    # 1 2 2
    # 2 2 1
    # 2 1 2        8 ways
    
    # #4
    # 1 1 1 1
    # 1 1 2
    # 1 2 1
    # 2 1 1
    # 2 2        5 ways
    # #3
    # 1 1 1
    #  1 2 
    #  2 1       3 ways
      
    #   #2
    #   1 1
    #   2        2 ways

    #   #1 
    #   1        1 ways
    #   #0
    #            1 ways