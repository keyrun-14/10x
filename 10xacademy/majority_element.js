let fs = require("fs");
let data = fs.readFileSync("input.txt", 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}
// // -------- Do NOT edit anything above this line ----------
function majority(n,arr){
    let d={}
for (i of arr){
    if (i in d){
        d[i]=d[i]+1       
    } else{
        d[i]=1
    }
}
let output='NONE'
for (value in d){
    if (d[value]>parseInt(n/2)){
        output=value
        }
}
console.log(output)
}
let n=parseInt(readLine());
let arr=readLine().split(" ").map(x=>parseInt(x));
majority(n,arr)

