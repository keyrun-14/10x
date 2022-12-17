for i in range(int(input())):
    n=int(input())
    steps=input()
    count=0
    height=0
    for i in range(n):
        if steps[i]=="U":
            height=height+1
            if height==0:
                count=count+1
        else:
            height=height-1
    print(count)
