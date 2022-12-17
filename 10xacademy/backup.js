let fs = require("fs");
let data = fs.readFileSync("input.txt", 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}
// // -------- Do NOT edit anything above this line ----------
let n=parseInt(readLine());
let arr=[]
for(let i=0;i<n;i++)
{
    a=parseInt(readLine());
    arr.push(a);
}
let x=parseInt(readLine());
let output=0
for(let i=0;i<n;i++)
{
    if(x>arr[i])
    {
        output=output+arr[i]
    }
}console.log(output)
