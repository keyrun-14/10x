M = int(input())
N = int(input())
if M == N:
    print(0)
else:
    count=0
    while (1 & M) == (1 & N):
        M>>=1
        N>>=1
        count += 1
    count += 1
    print(count)

M = int(input())
N = int(input())
if M == N:
    print(0)
else:
    temp = 1
    count = 1
    while (temp & M) == (temp & N):
        temp <<= 1
        count += 1

    print(count)