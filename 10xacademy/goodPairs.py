from collections import Counter


array=list(map(int,input().split()))

d=Counter(array)
sum=0
for key, value in d.items():   
    if value >=2:
        a=((value-1)*((value-1)+1))//2
        sum=sum+a
print(sum)