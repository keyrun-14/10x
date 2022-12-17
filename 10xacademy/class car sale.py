class Design():
    def __init__(self,n):
        self.no=n

    def getCustomerInput(self):
        for i in range(self.no):
            a.append(int(input()))
            if a[i]>=value*0.09:
                b.append(a[i])
                print(i)
        else:
            if len(b)==0:
                print(-1)
n=int(input())
a=[]
b=[]
value=1000000
sell=Design(n)
sell.getCustomerInput()