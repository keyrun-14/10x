c=input()
b=[]
a=c.lower()
for i in a:
    if 'a'<=i<='z' or '0'<=i<='9':
        b.append(i)
print(b)

d=b.reverse()#b[::-1]
print(d)
if b==d:
    print(True)
else:
    print(False)


b[2::]