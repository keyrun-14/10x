from argparse import RawDescriptionHelpFormatter


n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
count=1
max_area=0
for i in range(1,n):
    area=(arr[i-1]*count)
    if area>max_area:
        max_area=area
    if arr[i-1]<arr[i]:
        count=1

    count+=1

