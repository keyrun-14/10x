n=int(input())
number=[]
flag=0
for i in range(n):
    number.append(int(input()))
if number[0] >= 1:
    for j in range(0,n-1,2):
        if number[j] >= 1 and number[j+1]==0 and  (number[-1]==0 and n%2==0):
            flag=1
        else:
            flag=0
if number[0]==0:
    for i in range(0,n-1,2):
        if number[i]==0 and number[i+1]>=1 and (number[-1]>=1 and n%2==0):
            flag=1
        else:
            flag=0
if flag==1:
    print(True)
else:
    print(False)



n=int(input())
number=[]
flag=0
for i in range(n):
    number.append(int(input()))
if number[0] >= 1:
    for j in range(0,n-1,2):
        if number[j] >= 1 and number[j+1] == 0 and ((number[-1] >= 1 and n%2!=0) or (number[-1]==0 and n%2==0)):
            flag=1
        else:
            flag=0
if number[0]==0:
    for i in range(0,n-1,2):
        if number[i]==0 and number[i+1]>=1 and ((number[-1]>=1 and n%2==0) or (number[-1]==0 and n%2!=0)):
            flag=1
        else:
            flag=0
if flag==1:
    print(True)
else:
    print(False)




n=int(input())
number=[]
flag=0
for i in range(n):
    number.append(int(input()))
if number[0] >= 1:
    for j in range(0,n-1,2):
        if number[j] >= 1 and number[j+1]<=0 and ((number[-1] >= 1 and n%2!=0) or (number[-1]<=0 and n%2==0)):
            flag=1
        else:
            flag=0
if number[0]<=0:
    for i in range(0,n-1,2):
        if number[i]<=0 and number[i+1]>=1 and ((number[-1]>=1 and n%2==0) or (number[-1]<=0 and n%2!=0)):
            flag=1
        else:
            flag=0
if flag==1:
    print(True)
else:
    print(False)

