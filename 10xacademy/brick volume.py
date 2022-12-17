def brickvol(n,b,h):
    l=100
    if b==-1:
        b=60
    if h==-1:
        h=40
    brickvol=round(n*l*b*h*0.00005)
    return brickvol
n=int(input())
b,h=input().split()
b,h=float(b),float(h)
print(brickvol(n,b,h))