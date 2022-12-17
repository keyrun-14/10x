# def recursive_multiply(n):
#     if n<=9:     #12345>9    1234>9  123>9 12>9  1<9
#         return n # return 1
#     return n%10 * recursive_multiply(n//10)  #12345%10=5 * recursive cal(12345//10=1234)l, 1234%10=4  => 5*4 * RC(1234//10=123),5*4*3 * rc(123//10=12)   5*4*3*2  *rc(12//10)
# t=int(input())
# for i in range(t):
#     n=abs(int(input()))    # n=12345
#     print(recursive_multiply(n))  #5*4*3*2*1 =120

# d = {}
# arr = [1, 2, 3, 4, 5, 3,2, 1]
# for i in arr:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1

# abcd dcab adcb abdc
T = 'geeks'
a, b, c, d, e,f = input().split()
b = c = '*'
T = (a, b, c, d, e,f)
print(T)

