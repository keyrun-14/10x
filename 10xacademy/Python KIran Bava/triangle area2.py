#area of triangle
a=input("enter the value of side1    ")
b=input("enter the value of side2    ")
c=input("enter the value of side3    ")
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("area of triangle is  ",area)
