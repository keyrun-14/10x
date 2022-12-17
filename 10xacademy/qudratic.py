n=int(input())
while n>0:
    x,y=input().split()
    x,y=int(x),int(y)
    n=n-1
    if x > 0 and y > 0:
        print("Q1")
    elif x < 0 and y > 0:
        print("Q2")
    elif x < 0 and y < 0:
        print("Q3")
    elif x > 0 and y < 0:
        print("Q4")