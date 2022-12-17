# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
n=int(input())
a=1
for i in range(32):
    a=2**i
    if n==a:
        print("true")
        break
else:
    print("false")