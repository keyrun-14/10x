def jumping(arr,i,count,res):
    if i>=len(arr):
        res.append(count)
        return
    jumping(arr,i+1,count+1,res)       #selecting
    jumping(arr,i+arr[i],count+1,res)  #not selecting
n=int(input())
arr=[int(x) for x in input().split()]
res=[]
jumping(arr,0,0,res)
print(min(res))





##