for i in range(int(input())):
    n=input()
    n=list(n)
    arr=[]
    arr.append(n[0])
    for i in range(1,len(n)):
        if len(arr)==0:
            arr.append(n[i])
        elif n[i]!=arr[-1]:
            arr.append(n[i])
        else:
            arr.pop()
    if len(arr):
        print("".join(arr))
    else:
        print("KHALI")