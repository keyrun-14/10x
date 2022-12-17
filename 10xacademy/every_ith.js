let fs = require("fs");
const { arrayBuffer } = require("stream/consumers");
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
for(let i=0;i<n;i++){
    let input=parseInt(readLine());
    arr.push(input)
}
let sum=0
let index=parseInt(readLine());
if(index>0){
for(i=index-1;i<n;i=i+index){
    sum=sum+arr[i]
}
console.log(sum)
}else{
    console.log(0)
}