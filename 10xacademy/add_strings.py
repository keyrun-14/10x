# def addStrings(num1,num2):
#     num1=num1[::-1]
#     num2=num2[::-1]
#     if len(num2)>len(num1):
#         num1,num2=num2,num1
#     output=[]
#     carry=0
#     for i in range(len(num2)):
#         print("num1 ",num1[i],"   ","num2  ",num2[i])
#         sum=int(num2[i])+int(num1[i])+carry
#         carry=sum//10
#         output.append(sum%10)
#         print("sum = ",sum,"  ","carry = ",carry)
    
#     for i in range(len(num2),len(num1)):
#         print("num1 ",num1[i])
#         sum=int(num1[i])+carry
#         carry=sum//10
#         output.append(sum%10)
#         print("sum = ",sum,"  ","carry = ",carry)
#     if carry>0:
#         output.append(carry)
#     for i in range(len(output)-1,-1,-1):
#         print(output[i],end="")
#     print()
# for i in range(int(input())):
#     num1,num2=input().split()
#     print(num1 , " + " ,num2, " = ",int(num1)+int(num2))
#     addStrings(num1,num2)

def addStrings(num1,num2):
    if len(num2)>len(num1):
        num1,num2=num2,num1
    output=[]
    carry=0
    for i in range(len(num2)-1,-1,-1):
        sum=int(num2[i])+int(num1[i])+carry
        carry=sum//10
        output.append(sum%10)
    
    remaining=len(num1[:(len(num2))])
    for i in range(remaining-1,-1,-1):
        sum=int(num1[i])+carry
        carry=sum//10
        output.append(sum%10)
    if carry>0:
        output.append(carry)
    for i in range(len(output)-1,-1,-1):
        print(output[i],end="")
for i in range(int(input())):
    num1,num2=input().split()
    addStrings(num1,num2)