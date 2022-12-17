class Circle:
    pi=3.14
    def __init__(self,r):
        self.radius=r
    

    def getArea(self):
        if r<0:
            return 0.0
        else:
            area=Circle.pi*self.radius**2
            return area


    def getCircumference(self):
        if r<0:
            return 0.0
        else:
            circum=2*Circle.pi* self.radius
            return circum

r=float(input()) 
main=Circle(r)
print(main.getArea())
print(main.getCircumference())
