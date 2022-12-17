def gcd(x, y):
   while(y):
       x, y = y, x % y
   return x
def find_lcm(arr,n):
    lcm=arr[0]
    for i in range(1,n):
        lcm=(lcm*arr[i])//gcd(lcm,arr[i])
    return lcm
n=int(input())
arr=list(map(int,input().split()))
print(find_lcm(arr,n))