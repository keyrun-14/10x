n=int(input())
sum=0
for i in range(n):
    ele=int(input())
    sum=sum+ele
avg=sum/n
if avg>100:
    print("Excellent!")
else:
    print("Not Excellent!")

   
