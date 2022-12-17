# for i in range(int(input())):    
#     t=int(input())
#     a=list(map(int,input().split()))
#     b=[]
#     i=0
#     j=1
#     count=1
#     while i<j and j<len(a):
#         if a[i]<a[j]:
#             b.append(a[j])
#             i+=1
#             j=i+1
#             count=1
#         else:
#             j+=1
#             count=count+1
#     b=b+([-1]*count)
#     print(*b)


# for i in range(int(input())):    
#     t=int(input())
#     a=list(map(int,input().split()))
#     b=[]
#     for i in range(len(a)):       
#         for j in range(i+1,len(a)):
#             if a[i]<a[j]:
#                 b.append(a[j])
#                 break                
#         else:
#             b.append(-1)                
#     print(*b)


for i in range(int(input())):    
    t=int(input())
    a=list(map(int,input().split()))
    output=[-1]
    stack=[a[-1]]
    for i in range(len(a)-2,-1,-1):
        if a[i]<stack[-1]:
            output.append(stack[-1])
            stack.append(a[i])        
        elif a[i]>=stack[-1]:
            while len(stack)>0 and a[i]>=stack[-1]:
                stack.pop()            
            if len(stack)==0:
                output.append(-1)
                stack.append(a[i])
            else:
                output.append(stack[-1])
                stack.append(a[i])
    output=output[::-1]
    print(*output)

