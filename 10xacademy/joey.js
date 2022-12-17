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
a=parseInt(readLine());
temp=a;
for(let i=0;i<n-1;i++){
    b=parseInt(readLine());
    temp=temp+b
}
let avg=Math.floor(temp/n);

console.log(avg)
if (avg<25){
    console.log(true)
}else{
    console.log(false)
}