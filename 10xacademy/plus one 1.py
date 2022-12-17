
a=list(map(int,input()))

for i in range(len(a)):
    rem=a[i]%10
    b=rem+1
    a[len(a)-1]=b
print(a) 