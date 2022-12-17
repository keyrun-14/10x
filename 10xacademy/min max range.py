# def min_max_range(a,b,c):
def minin(a):                                                               
    m1=min(a)
    return m1                                                           
def maxin(b):
    m2=max(b)
    return m2
def min_max_range(c,d):
    m1=minin(a)
    m2=maxin(b)
    if m1>m2:
        m1,m2=m2,m1
    for x in c:
        if m1<=x<=m2:
            d.append(x)
    else:
        if x<m1 and x>m2:
            print(-1)
    for i in d:
        print(i)
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
d=[]
minin(a)
maxin(b)
min_max_range(c,d)

def minin(a):
    m1=min(a)
    return m1
def maxin(b):
    m2=max(b)
    return m2
def min_max_range(c,x,y):
    m1=x
    m2=y
    d=[]
    if (m1>m2):
        m1,m2=m2,m1
    for x in c:
        if m1<=x<=m2:
            d.append(x)
    if(len(d)==0):
        print(-1)
    for i in d:
        print(i)
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
x=minin(a)
y=maxin(b)
min_max_range(c,x,y)