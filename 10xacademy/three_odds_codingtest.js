const { count } = require("console");
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
let count1=0
for(let i=0;i<n;i++)
{
    let a=parseInt(readLine());
    
    if(a%2 != 0)
    {
        count1=count1+1
    }
    else if(count1===3)
    {
        console.log("True")
        break;
    }
    else
    {
        count1=0
    }

}
if (count1 != 3)
{
    console.log("False")
}
