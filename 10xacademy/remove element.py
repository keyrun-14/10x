a=list(map(int,input().split()))
target=int(input())
for i in range(a.count(target)):
    a.remove(target)
    a.append("_")
print(a)