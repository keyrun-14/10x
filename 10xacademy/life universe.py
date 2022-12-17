'''
#n=int(input())
a= list(map(int,input("\n").split()))
#k=0
for i in range(100):
    k=a[i]
    if a[i]==42:
        break
    else:
        print(a[i])
'''
while True: 
    n=int(input())
    if n==42:
        break
    else:
        print(n)
n=int(input())
while n!=42:
    print(n)
    n=int(input())

