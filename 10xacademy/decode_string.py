# s=input()
# s=list(s)
# stack=[]
# output=[]
# temp=""
# for i in range(len(s)):
#     if s[i].isnumeric():
#         output.append(s[i])
#     if s[i]=="[":
#         continue
#     elif s[i].isalpha():
#         stack.append(s[i])
#     elif s[i]=="]":
#         stack_pop=stack.pop()
#         output_pop=output.pop()
#         temp=temp+(stack_pop)
#         temp=int(output_pop)*temp
# print(temp[::-1])



s=input()
s=list(s)
stack=[]

temp=""
for i in range(len(s)):
    if s[i]!="]":
        stack.append(s[i])
    if s[i]=="]":
        while 
print(temp[::-1])

# ##    3[a[2[c]]        3* acc
#       accaccacc