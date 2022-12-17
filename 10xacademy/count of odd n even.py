n=int(input())
count1=0
count2=0
for i in range(n):
    a=int(input())
    if a%2==0:
        count1=count1+1
    if a%2!=0:
        count2=count2+1
print(count2)
print(count1)

