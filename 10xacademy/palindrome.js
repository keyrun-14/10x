let fs = require("fs");
let data = fs.readFileSync("input.txt", 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}
// // -------- Do NOT edit anything above this line ----------
let l=parseInt(readLine());
let a=l
let s=0
if (l<0){
    console.log(-1)
}else{
do{
    reminder=a%10
    s=s*10+reminder
    a=parseInt(a/10)
}while (a>0);
}
if (s===l){
    console.log(true)
}else{
    console.log(false)
}
