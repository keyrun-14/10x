let fs = require("fs");
let data = fs.readFileSync("input.txt", 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}

// -------- Do NOT edit anything above this line ----------

let number = parseInt(readLine())
let amstrong = 0
let temp = number;
while (temp>0)
{
let a =temp%10;
amstrong = amstrong+(a*a*a);
temp=Math.floor(temp/10);
}
if(amstrong==number)
{
    console.log("Yes");
}
else{
    console.log("No");
}