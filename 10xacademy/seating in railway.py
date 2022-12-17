n=int(input())
for i in range(n):
    c,b=input().split()
    c,b=int(c),int(b)
    k=b%8
    if c>=b and b>0:        
        if k==1 or k==4:
            print("L")
        elif k==2 or k==5:
            print("M")
        elif k==3 or k==6:
            print("U")
        elif k==7:
            print("SL")
        elif k==0:
            print("SU")
    else:
        print("Invalid")