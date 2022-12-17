let fs = require("fs");
let data = fs.readFileSync("input.txt", 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}
// // -------- Do NOT edit anything above this line ----------

let inputs=readLine().split(" ").map(x=>parseInt(x))
let keyboards=readLine().split(" ").map(x=>parseInt(x)).slice(0,inputs[1])
let usbs=readLine().split(" ").map(x=>parseInt(x)).slice(0,inputs[2])
let costs=[]
for(let i=0;i<keyboards.length;i++)
{
    for(let j=0;j<usbs.length;j++)
    {
        sum=keyboards[i]+usbs[j]
        costs.push(sum)
    }
}
costs.sort(function (a,b){return b-a})

let flag=0
for(let i=0;i<costs.length;i++)
{
    if(costs[i]<=10)
    {
        console.log(costs[i])
        flag=1
        break;
    }
}if(flag==0)
{
    console.log(-1)
}