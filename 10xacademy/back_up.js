let arr=[3,2,5,10,8];
console.log()
let query=4;
let sum=0;
for(let i=0;i<arr.length;i++)
{
    if (arr[i]<query)
    {
        sum=sum+arr[i]
    }
}
console.log(sum)