n=input()
count1=0
count2=0
for i in range(len(n)):
    if n[i]=="G":
        count1=count1+1
    if n[i]=="R":
        count2=count2+1
if count1>count2:
    print(count2)
   
else:
    print(count1)
