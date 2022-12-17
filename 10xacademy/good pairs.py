# a=list(map(int,input().split()))
# count=0
# for i in range(len(a)-1):
#     for j in range(i+1,len(a)):
#         if a[i]==a[j] and i<j:
#             count=count+1
# print(count)
def goodpairs(a):
    count=0
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if a[i]==a[j] and i<j:
                count=count+1
    return count
a=list(map(int,input().split()))
print(goodpairs(a))
