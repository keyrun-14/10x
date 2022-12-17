s=input()
n=s.split(" ")
for i in n:
    count=0
    for j in range(len(i)-1,0,-1):
        if i[j]==i[j-1]:
            count=count+1
    print(i[:len(i)-count],end=" ")
