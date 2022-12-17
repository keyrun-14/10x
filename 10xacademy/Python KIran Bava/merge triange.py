
method=input("choose method  x , y")
if method=="x":
    print("area=0.5*b*h")
    b=float(input("enter the value b "))
    h=float(input("enter the value  h  "))
    area=0.5*b*h
    print(" area is ",area)
elif method=="y":
    print("area= (s*(s-a)*(s-b)*(s-c))**0.5 ")
    a=float(input("enter the value a "))
    b=float(input("enter the value b "))
    c=float(input("enter the value c "))
    s=(a+b+c)/2
    area= (s*(s-a)*(s-b)*(s-c))**0.5
    print(" area is ",area)
else:
         print("select x or y")
    
