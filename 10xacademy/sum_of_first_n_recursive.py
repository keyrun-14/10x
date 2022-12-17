def sumOffirstN(n,psum):
    if n==1:
        print(n,1)
        return 1
    psum=psum+n+sumOffirstN(n-1,psum)
    print(n,psum)
    return psum
n=int(input())
psum=0
sumOffirstN(n,psum)


# a="kiran"
# res=""
# for i in a:
#     res=i+res
#     print(res)
# print(res)

def something(a):
    return a
print("kiran")

print(something("kiran"))