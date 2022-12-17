num1=list(map(int,input().split())) ## [1,2,2,1]  ## len=4
num2=list(map(int,input().split())) ## [2,2]     ## len=2
if len(num1)>len(num2):   ##4>2
    num1,num2=num2,num1  ##num1=num2   ## num2=num1
d={}

print("num1 array is ",num1)
print("num2 array is ",num2)
for i in range(len(num2)):  ##[1,2,2,1]  ## d={ 1:2,2:2}
    if num2[i] in d:
        d[num2[i]]=d[num2[i]] + 1
    else:
        d[num2[i]]=1
output=set()
for i in range(len(num1)):##[2,2]
    if num1[i] in d:    ##### d={ 1:2,2:2}
        output.add(num1[i])


print(output)