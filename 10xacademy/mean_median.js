let fs = require("fs");
let data = fs.readFileSync("input.txt", 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}


let t=parseInt(readLine());
for(let i=0;i<t;i++)
{
    let n=parseInt(readLine());
    let arr=readLine().split(" ").map(x=>parseInt(x)).slice(0,n);
    arr.sort(function(a,b){return a-b});
    let sum=0
    let output=[]
    for(let j=0;j<n;j++)
    {
        sum=sum+arr[j]
    }
    output.push((parseInt(sum/n)));
    if(n%2 != 0)
    {
        output.push(arr[parseInt(n/2)])
    }
    else if(n%2==0)
    {   x=parseInt((arr[n/2]+arr[(n/2)-1])/2);
        //console.log(x)
        output.push(x)
    }
    else if (n==1)
    {
        output.push(arr[0])
    }

    console.log(output.join(" "))
}