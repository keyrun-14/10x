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
let sum=0
for(let i=0;i<n;i++)
{
    a=parseInt(readLine());
    sum=sum+a
}
let avg=sum/n
if(avg>100)
{
    console.log("Excellent!")
}
else
{
    console.log("Not Excellent!")
}