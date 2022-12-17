n=int(input())
past=list()
while n!=1:
    n=sum(int(i)**2 for i in str(n))
    print(n)
    if n in past:
        print(False)
    else:
        print(True)
past.append(n)
