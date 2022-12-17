n=int(input())
for i in range(n):
    string=input()
    L=len(string)
    count=0
    for i in range(L//2):
        if string[i]==string[L-1-i]:
            count=count+1
