# 14541
# 14541
# True
# 134
# 431
# False
# -121
# abs
# 121
# -121
# 121%10==1 #n=121
# a=121
# 121//10
# 12     #n=12
# 12%10==2
# 12//10
# 1
# if n==a: then True
# else: False
a=int(input())
n=a        
pal=0      
while n>0:           
    rem=n%10           
    pal=pal*10+rem      
    n=n//10              
if pal==a: 
    print(True)
else:
    print(False)