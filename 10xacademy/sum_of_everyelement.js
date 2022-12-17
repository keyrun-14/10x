let fs = require("fs");
let data = fs.readFileSync("input.txt", 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}
// // -------- Do NOT edit anything above this line ----------
let n =parseInt(readLine());
if (n>0)
{
    let arr=[]
    for (let i=0;i<n;i++)
    {
        arr.push(parseInt(readLine()));
    }
    let query=parseInt(readLine());
    let sum=0;
    if (query>0)
    {
        for(let j=0;j<n;j++)
        {
            if(arr[j]%query===0)
            {
                sum=sum+arr[j]
            }
        }
        console.log(sum)
    }
}
