let fs = require("fs");
let data = fs.readFileSync("input.txt", 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}
// // -------- Do NOT edit anything above this line ----------
let a=readLine().split(" ")
let b=0
for(let i=0;i<(a.length)-1;i++)
    {
    if (a[i].length>b){
        b=a[i].length
    }
}
console.log(b)