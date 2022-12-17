num1,num2=input().split()
num1,num2=int(num1),int(num2)
time=num1+num2
if (0<time<=12):
        print(time)
elif (0<num1<=12) and (0<num2<=12) and (12<time<=24):    
        x=time-12
        print(x)