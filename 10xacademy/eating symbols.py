s=input()
mind1=0
mind2=0
for i in range(len(s)):
    if s[i]=="+":
        mind1=mind1+1
    elif s[i]=="-":
        mind2=mind2-1
print(mind1+mind2)
