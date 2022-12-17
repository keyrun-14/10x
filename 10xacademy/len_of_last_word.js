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

if (a.length==0)
{
    console.log(0)
}
else{
    console.log(a[a.length-1].length,"Length of the last word is length of",a[a.length-1],"which is",a[a.length-1].length)
}
