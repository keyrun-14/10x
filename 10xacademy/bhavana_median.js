let fs = require("fs");
let data = fs.readFileSync("input.txt", 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}
// // -------- Do NOT edit anything above this line ----------

let t=parseInt(readLine())
while(t>0)
{
    let n=parseInt(readLine())
    let a=readLine().split(" ")
    res=[]
    let mean;
    let median;
    a.sort(function(a,b){return a-b});
    let sum=0
    let lefthalf=parseInt(n/2)
    for(let i=0;i<n;i++)
    {
    sum=sum+parseInt(a[i])
    }
    mean=parseInt(sum/n)
    res.push(mean)
    if(n%2===0)
    {
        median=parseInt((parseInt(a[lefthalf])+parseInt(a[lefthalf-1]))/2)
        console.log(median)
        console.log(a[lefthalf],a[lefthalf-1])
    }
    else
    {
        median=a[lefthalf]+"10"
    }
    res.push(median)
    console.log(res.join(" "))
    t--;
}