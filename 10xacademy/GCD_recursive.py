def gcd(dividend,divisor):
    if dividend % divisor==0:
        return divisor
    return gcd(divisor,dividend % divisor)
if __name__ == "__main__":
    n=int(input())
    for index in range(n):
        inputInts = input().split(' ')
        dividend = int(inputInts[0])
        divisor = int(inputInts[1])
        print(gcd(dividend,divisor))
# a=int(input())
# b=int(input())
# print(GCD(a,b))