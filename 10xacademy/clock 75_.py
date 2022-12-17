num1,num2=input().split()
num1,num2=int(num1),int(num2)
time=num1+num2
x=0
if 0<time<=12:
    print(time)
elif time>=12:
     x=time-12
     print(abs(x))