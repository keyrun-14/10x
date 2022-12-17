# n=int(input())
# res=[]
# while n>0:
# 	a=n%2
# 	res.append(a)
# 	n=n//2
# sum=0
# for i in range(1,len(res)-1):
# 	if res[i]==0:
# 		res[i]=1
# 	else:
# 		res[i]=0
# for i in range(len(res)):
# 	sum=sum+res[i]*2**i
# print(sum)
n=int(input())
duplicate=n
t=2
incr=2
if n<4:
    print(n)
else:
    while duplicate>1:
        n^=t
        t=2*t
        duplicate>>=incr
        incr=1
    print(n)