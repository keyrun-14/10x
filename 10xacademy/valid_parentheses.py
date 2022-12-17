s=input()
a,b="(",")"
x,y="{","}"
p,q="[","]"
flag="false"
if len(s)>1:
    for i in range(0,len(s),2):
        if s[i]==a and s[i+1]==b or s[i]==x and s[i+1]==y or s[i]==p and s[i+1]==q:
            flag="true"
        else:
            flag="false"
            break
    print(flag)

class Solution:
    def isValid(self, s: str) -> bool:
      
        flag="false"
        if len(s)>1:
            for i in range(0,len(s),2):
                if s[i]==a and s[i+1]==b or s[i]==x and s[i+1]==y or s[i]==p and s[i+1]==q:
                    flag="true"
                else:
                    flag="false"
                    break

               
            return flag
s=input()
a,b="(",")"
x,y="{","}"
p,q="[","]"
valid=Solution()
print(valid.isValid(s))
