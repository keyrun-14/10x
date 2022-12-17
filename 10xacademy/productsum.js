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
let a=n

if (n>0){
    let sum=0
    let product=1
    while (a>0){
        reminder=a%10
        sum=sum+reminder
        product=product*reminder
        a=parseInt(a/10)

    }console.log(product-sum)
}else{
    console.log(0)
}

