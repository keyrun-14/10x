num1,num2=input().split()
num1,num2=int(num1),int(num2)
n=num1+num2
n=n%12
if n==0:
    print(12)
else:
    print(n)