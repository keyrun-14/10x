# 1 3 6 9 8 6
# max product = 9*8*6
# 2 5 7 -12 77 -10 31
# max product = 77*31*7
# 2 5 7 -12 7 -100 7
# max product= -12*-100*7
# 1 3 6 9 8 6
# sort 1 3 6 6 8 9
# max product = 77*31*7
# 2 5 7 -12 7 -100 7
# sort -100 -12 2 5 7 7

# -100*-12*7
# a[0]*a[1]*a[-1]
# a[-1]*a[-2]*a[-3]
# max(a[0]*a[1]*a[-1],a[-1]*a[-2]*a[-3])
# a
# def maxproduct(a):
#     a.sort()
#     print(max(a[0]*a[1]*a[-1],a[-1]*a[-2]*a[-3]))
# a=list(map(int,input().split()))
# maxproduct(a)

# r=10   pi==3.14
# area of circle =pi*r**2===314
# preimeter of circle= 2*pi*r
class circle:
    def __init__(self,r):
        self.radius=r
    def areaofcircle(self,r):        
        if r>0:
            area=3.14*r**2
            return round(area,2)
        else:
            return 0.0
    def perimeterofcircle(self,r):
        if r>0:
            perimeter=2*3.14*r
            return round(perimeter,2)
        else:
            return 0.0
r=float(input())
circle1=circle(r)
print(circle1.areaofcircle(r))
print(circle1.perimeterofcircle(r))