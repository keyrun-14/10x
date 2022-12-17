n=int(input())
if n>0:
    a=int(input())
    count=1    
    for i in range(1,n):
        ele=int(input())
        if a==ele:
            count=count+1
    print(count)
else:
    print("invalid")