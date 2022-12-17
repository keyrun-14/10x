
# n=list(map(int,input().split()))
# sum=0
# b=[]
# a=[]
# for i in range(len(n)-2):
#     for j in range(1,len(n)-1):
#         for k in range(2,len(n)):
#             sum=n[i]+n[j]+n[k]
#             if sum==0:
#                 if i != j and i != k and j != k:
#                     a.extend([n[i],n[j],n[k]])
#                     b.append(a)
#                     a.clear(a)       
# print(b)

class Rectangle:
    def __init__(self,l,w):
        self.length=l
        self.width=w
    def rectangle_area(self):
        if self.length<=0 and self.width<=0:
            return 0
        else:
            area=self.length*self.width
            return area 
    def rectangle_perimeter(self):
        if self.length<=0 and self.width<=0:
            return 0
        else:
            perimeter=2*(self.length+self.width)
            return perimeter
l=int(input())
w=int(input())
rectangle1=Rectangle(l,w)
print(rectangle1.rectangle_area())
print(rectangle1.rectangle_perimeter())