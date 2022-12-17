num_of_pixels = int(input())
pix = []
for i in range(num_of_pixels):
    pix.append(int(input()))
m = int(input())
icon = []
Count=0
for i in range(m):
    icon.append(int(input()))
while(len(pix)>m):   
     flag=1
     for i in range(0,m):
          if pix[i]!=icon[i]:
               flag=0
               break
     if(flag==1):
          Count+=1
          pix=pix[m::]
     else:
          pix=pix[1::]
print(Count)