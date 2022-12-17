const { captureRejectionSymbol } = require("events");
let fs = require("fs");
let data = fs.readFileSync("input.txt", 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}

// -------- Do NOT edit anything above this line ----------
let n=parseInt(readLine());
for(let i=0;i<n;i++)
{
  let num1=readLine().split(" ").map(x=>parseInt(x))
let num2=readLine().split(" ").map(x=>parseInt(x))
if (num2.length>num1.length)
{
    a=num1
    num1=num2
    num2=a
}
let output=[]
let carry=0
let sum=0

for(let i=0;i<num1.length;i++)
{
  if(i<num2.length)
  {
    sum=num1[i]+num2[i]+carry;
  }
  else
  {
    sum=num1[i]+carry;
  }
  carry=parseInt(sum/10)
  output.push(sum%10);
}
if (carry>0)
{
  output.push(carry)
}
console.log(output.join(""))

}
