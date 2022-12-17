let t=parseInt(readLine());
for(let i=0;i<t;i++)
{
    let n=parseInt(readLine());
    arr=readLine().split(" ");
    let sum=0;
    for(letj=0;j<n;j++)
    {
        sum=sum+parseInt(arr[i]);
    }
    avg=sum/n;
    let count=0
    for(let k=0;k<n;k++)
    {
        if (avg<parseInt(arr[k]))
        {
            count=count+1
        }
    }
    console.log(count)
}