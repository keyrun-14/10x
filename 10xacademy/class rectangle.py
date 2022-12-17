class Rectangle():
    def __init__(self,l,w):
        self.length=l
        self.width=w
    def rectangle_area(self):
        if self.length>0 and self.width>0:
            area=self.length*self.width
            return area
        else:
            return 0
    def rectangle_perimeter(self):
        if self.length>0 and self.width>0:
            perimeter=2*(self.length+self.width)
            return perimeter
        else:
            return 0
l=int(input())
w=int(input())
rect=Rectangle(l,w)
print(rect.rectangle_area())
print(rect.rectangle_perimeter())