for i in range(int(input())):
    n=int(input())
    girls=list(map(int,input().split()))[:n]
    girls.sort()
    boys=list(map(int,input().split()))[:n]
    boys.sort(reverse=True)
    count=0
    for i in range(n):
        if girls[i]%boys[i]==0 or boys[i]%girls[i]==0:
            count=count+1
    print(count)
