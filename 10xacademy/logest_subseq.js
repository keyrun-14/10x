let arr=[6,7,3,1,100,102,6,12]
// let arr=[5,6,1,2,8,9,7]
arr.sort((a,b) => a-b)
let count=1
let maxx=Number.MIN_VALUE
for(let i=0;i<arr.length-1;i++){
if(arr[i+1]-arr[i]==1){
    count+=1
}else{
    if(count>maxx){
        maxx=count
    }
    count=1
}
}
if(count>maxx){
    maxx=count
}
console.log(maxx)
