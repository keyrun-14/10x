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
let arr=readLine().split(" ").map(x=>parseInt(x)).slice(0,n);
arr.sort(function(a,b){return b-a})
console.log(arr)
let diff=99999999999999;
for(let i=0;i<n-1;i++)
{
    min_diff=arr[i]-arr[i+1]
    if (min_diff<diff)
    {
        diff=min_diff
    }
}console.log(diff)