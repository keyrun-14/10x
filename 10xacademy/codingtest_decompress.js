let fs = require("fs");
let data = fs.readFileSync("input.txt", 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}
// // -------- Do NOT edit anything above this line ----------

let a=parseInt(readLine());
let arr=[]
for(let i=0;i<a;i++)
{
b=parseInt(readLine());
arr.push(b)
}
if(arr.length%2==0 && arr.length>=2 )
{
for(let j=0;j<a;)
{
    sum=arr[j]*String(arr[j+1])
    console.log(sum)
    j=j+2;
  }
}
 

