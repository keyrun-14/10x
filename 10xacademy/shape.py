class Rectangle():
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def calculatePerimeter(self,length,width):
        perimeter=2*(self.length+self.width)
        return perimeter
length,width=input().split()
length,width=int(length),int(width)
perimeter1=Rectangle(length,width)
per=perimeter1.calculatePerimeter(length,width)
print(per)


