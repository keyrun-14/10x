n=int(input())
for i in range(n):
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    if len(a)<len(b):
        a,b=b,a
    carry=0
    j=0
    sum=0
    output=[]
    for i in range(len(a)):
        if j<len(b):
            sum=a[i]+b[j]+carry
        else:
            sum=a[i]+carry
        if sum>=10:
            carry=sum//10
            sum=sum%10
        else:
            carry=0
        j=j+1
        output.append(sum)
    if carry>0:
        output.append(carry)
    for i in output:
        print(i,end=" ")
    print()

# if i<len(num2):
#             sum1=int(num1[i])+int(num2[i])+carry
#         else:
#             sum1=int(num1[i])+carry
#         carry=sum1//10
#         res+=str(sum1%10)

# def addStrings(s1,s2):
#     num1=s1[::-1]
#     num2=s2[::-1]
#     res = ""
#     carry = 0
#     if len(num1) < len(num2):
#         num1,num2 = num2,num1   
#     for i in range(len(num1)):
#         if i<len(num2):
#             sum1=int(num1[i])+int(num2[i])+carry
#         else:
#             sum1=int(num1[i])+carry
#         carry=sum1//10
#         res+=str(sum1%10)     
#     if carry > 0:
#         res += str(carry)
#     return res[::-1]
# for i in range(int(input())):
#     num1,num2 = input().split()
#     print(addStrings(num1,num2))