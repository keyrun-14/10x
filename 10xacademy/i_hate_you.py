for i in range(int(input())):
    n=input()
    
    arr=[]
    while len(n)>0:
        j=0
        while j<=len(n)-2:
            if n[j]!=n[j+1]:
                arr.append(n[j])
                j+=1
            else:
                j+=2
        if n[-1]!=n[-2]:
            arr.append(n[-1])
        n=arr
    print(arr)