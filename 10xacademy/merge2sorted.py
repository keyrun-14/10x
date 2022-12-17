arr1=[6,7,8,9]
arr2=[1,2,3,4,5]
i,j=0,0
temp=[]
while i< len(arr1) and j< len(arr2):
    if arr1[i]<arr2[j]:
        temp.append(arr1[i])
        i+=1
    else:
        temp.append(arr2[j])
        j+=1
while i< len(arr1):
    temp.append(arr1[i])
    i+=1
while j< len(arr2):
    temp.append(arr2[j])
    j+=1
print(temp)


O(len(arr1))  
##DONE  [1, 2, 3, 4, 5, 6, 7, 8, 9]


