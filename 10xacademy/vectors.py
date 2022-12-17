a1,a2,a3=input().split()
a1,a2,a3=int(a1),int(a2),int(a3)
b1,b2,b3=input().split()
b1,b2,b3=int(b1),int(b2),int(b3)
AB=((a1*b1)+(a2*b2)+(a3*b3))
AxB=((((a2*b3)-(a3*b2))**2)-(((a1*b3)-(b1*a3))**2)+((a1*b2)-(a2*b1))**2)
if AB==0:
    print(2)
elif AxB==0:
    print(1)
else:
    print(0)