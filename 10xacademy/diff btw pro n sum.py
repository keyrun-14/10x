n=int(input())
a=n
sum=0
mul=1
while n>0:
    reminder=n%10
    sum=sum+reminder
    mul=mul*reminder
    n=n//10
if a==0:
    print(0)
else:
    print(mul-sum)
'''
while n>0:
    reminder=n%10
    mul=mul*reminder
    n=n//10
mul=mul*n
print(mul)
'''