# range is -10 to 10
# 0 1 2 3 4 5 6 7 8 9 10
# range is -19 to -2 # no positive integer in this range
# -1
# 11 to 21
# 11 12 13 ......  21
m=int(input())
n=int(input())
if m<0 and n<0:
    print(-1)
else:
    for i in range(m,n+1):
        if i >=0:
            print(i)
        # break
        # 
