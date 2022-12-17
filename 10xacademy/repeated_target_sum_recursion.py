def Repeated(arr,i,curr,target,result):
    if target==0 and i==len(arr):
        if curr not in result:
            result.append(curr)
        return
    elif(i==len(arr)or target<0):
        return
    Repeated(arr,i,curr + [arr[i]],target - arr[i],result)
    Repeated(arr,i+1,curr + [arr[i]],target - arr[i],result)
    Repeated(arr,i+1,curr,target,result)
n, k=[int(x) for x in input().split()]
arr=[int(x) for x in input().split()]
target=k
curr=[]
result=[]
Repeated(arr,0,curr,target,result)
print(len(result)) 
#repeatedtarget sum