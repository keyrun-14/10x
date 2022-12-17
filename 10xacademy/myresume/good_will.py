n=int(input())
array="$*$"
if n==1:
    print((" "*(n-1)+"*"))
elif n==2:
    print((" "*(n-1)+"*"))
    print((" "*(n-2)+"$*$"))
elif n>2:
    print((" "*(n-1)+"*"))
    print((" "*(n-2)+"$*$"))
    for i in range(3,n+1):
        if i%2!=0:
            array="*"+array+"*"
            print(" "*(n-i)+array)
        else:
            array="$"+array+"$"
            print(" "*(n-i)+array)

