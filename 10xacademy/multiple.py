N=int(input())
for i in range(1,10**9):
    if i%2==0 and i%N==0:
        print(i)
        break