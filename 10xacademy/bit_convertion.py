main=[]
for i in range(int(input())):
    n=int(input())
    res=[]
    while n>0:
        a=n%2
        res.append(a)
        print(n,"n")
        n=n//2
    
    reverse=res[::-1]
    print(i,"  ",reverse)
    main.append(reverse)
    # sum=0
    # for i in range(1,len(res)-1):
    #     if res[i]==0:
    #         res[i]=1
    #     else:
    #         res[i]=0
    # for i in range(len(res)):
    #     sum=sum+res[i]*2**i
    # print(sum)
# ############################################
#           ##  RIGHT MOST DIFF BIT ##  #
# ############################################
# def Right_most_diff_bit(c,d):
#     if len(d)>len(c):
#         c,d=d,c    
#     e=[]
#     count=0
#     for i in range(len(c)-1,-1,-1):
#         if i>len(d)-1:
#             d.insert(0,0)        
#         if c[i]!=d[i]:
#             count=i
#             break
#     print(count)
# Right_most_diff_bit(main[0],main[1])

    



# ############################################
#           ##  XOR  ## ^ #
# ############################################
# def XOR(c,d):
    
#     e=[]
#     for i in range(len(c)-1,-1,-1):
#         if i>len(d)-1:
#             d.insert(0,0)
#         if c[i]==d[i]:
#             e.append(0)
#         else:
#             e.append(1)
#     sum=0
#     for i in range(len(e)):
#         sum=sum+e[i]*2**i
#     print()
#     print("XOR operand ^  =",sum)
#     print()
# XOR(main[0],main[1])

# ##############################################
#            ## OR  ## | #
# ##############################################
# c=[1,1,1,1,1]
# d=[1,1,1,0]
# e=[]
# for i in range(len(c)-1,-1,-1):
#     if i>len(d)-1:
#         d.insert(0,0)
#     if c[i]==d[i]==1 or c[i]==1 or d[i]==1:
#         e.append(1)
#     else:
#         e.append(0)
# print(e)
# print()
# sum=0
# for i in range(len(e)):
#     sum=sum+e[i]*2**i
# print(sum)
# print()
# print("OR operand |  =",31|14)
# print()

# ###############################################
#                ## AND ## $ #
# ###############################################
# c=[1,1,1,1,1]
# d=[1,1,1,0]
# e=[]
# for i in range(len(c)-1,-1,-1):
#     if i>len(d)-1:
#         d.insert(0,0)
#     if c[i]==d[i]==1:
#         e.append(1)
#     else:
#         e.append(0)
# print(e)
# print()
# sum=0
# for i in range(len(e)):
#     sum=sum+e[i]*2**i
# print(sum)
# print()
# print("and operand &  =",31&14)
# print()






Can you please introduce yourself ?	What are your strength and weakness ?	What are your long term and short term goal ?	what is your expected CTC ?	WHy you choose yourself to be a software engineer ?	IF Experienced candoidate what is your curret CTC ?	On which coding language you have more experties ?