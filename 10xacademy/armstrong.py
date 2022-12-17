n=int(input())
num=n
sum=0
length=len(str(num))
print(length)
while num>0:
    reminder=num%10
    sum=sum + (reminder*reminder*reminder)
    num=num//10
if (n==sum):
    print("Yes")
else:
    print("No")