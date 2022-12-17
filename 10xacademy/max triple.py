n=int(input())
a=[]
# temp=0
# product1=0
# product2=0
if -1000<n<1000:
    for i in range(n):
        b=int(input())
        a.append(b)
a.sort()
if 3<=len(a)<10**4:
    print(max(a[0]*a[1]*a[-1],a[-1]*a[-2]*a[-3]))
    # for i in range(n-1):
    #     for j in range(i+1,n):
    #         if a[i]>a[j]:
    #             temp=a[i]
    #             a[i]=a[j]
    #             a[j]=temp 
    #product1=a[0]*a[1]*a[-1]
    #product2=a[-1]*a[-2]*a[-3]
    #print(max(a[0]*a[1]*a[-1],a[-1]*a[-2]*a[-3]))
    # if product1>product2:
    #     print(product1)
    # else:
    #     print(product2)
    