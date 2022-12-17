def beauty(arr):
    a = 0
    b = 0
    c = 0
    table = {}
    table[(a,b,c)] = 1
    for i in arr:
        if i == 'a':
            a+=1
        elif i == 'b':
            b+=1
        elif i == 'c':
            c+=1
        k = min(a,b,c)
        a-=k
        b-=k
        c-=k
        if(a,b,c) not in table:                                                     
            table[(a,b,c)] = 1
        else:
            table[(a,b,c)] += 1
    sum = 0
    for i in table.values():
        sum += (i*(i-1)) // 2
    return sum                       
t = int(input())
for i in range(t):
    str = input()
    print(beauty(str.strip()))