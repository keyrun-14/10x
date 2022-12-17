def binomialCoeff(n,r):
    if n>r:
        if r==0 or n==r:
            return 1
        return binomialCoeff(n-1,r-1) + binomialCoeff(n-1,r)
if __name__ == "__main__":
    numTcs = int(input())
    for index in range(numTcs):
        inputInts = input().split(' ')
        n = int(inputInts[0])
        r = int(inputInts[1])
        print(binomialCoeff(n, r))
# n=int(input())
# r=int(input())
# print(binomialCoeff(n,r))

# 5C2= 4C1 + 4C2 
# 4C1=3C0 + 3C1
# 3C1=2C0 + 2C1
# 2C1=1C0 + 1C1

# 4C2= 3C1 + 3C2
# 3C1=2C0 + 2C1
# 2C1=1C0 + 1C1
# 3C2=2C1 + 2C2
# 2C1=1C0 + 1C1
# 2C2= 1