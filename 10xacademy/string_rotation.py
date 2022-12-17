# for i in range(int(input())):
#     s1=input()
#     s2=input()
#     flag=0
#     for i in range(len(s1)):
#         if s1[i:]+s1[:i]==s2:
#             flag=1
#             break
#         else:
#             flag=0
#     if flag==1:
#         print(True)
#     else:
#         print(False)
# print(s1[3:]+s1[:3])



def isSubstring(s1, s2):
    if s1.find(s2) != -1:
        return True
    if s2.find(s1) != -1:
        return True
    return False

## Do not change anything above
def isRotation(s1,s2):
    ## You can only call isSubstring function from this function once. Use this function to check if s2 is a rotation of s1.
    if len(s1)==len(s2):
        if s1 in s2+s2: 
            print(isSubstring(s1,s2))
        else:
            print(False)
    else:
        print(False)
## Do not change anything below
t = int(input()) 
for i in range(t):
    s1 = input() 
    s2 = input()
    isRotation(s1,s2)