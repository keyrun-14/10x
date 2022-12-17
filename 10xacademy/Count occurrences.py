n=int(input())

a=[]
for i in range(n):
    b=int(input())
    a.append(b)
query=int(input())
print(a.count(query))