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
let max=parseInt(readLine());
let inputs=parseInt(readLine());
let arr=[]
for(let i=0;i<inputs;i++)
{
    arr.push(parseInt(readLine()));
}
for(let j=0;j<inputs;j++)
{
    for(let i=0;i<n;i++)
    {
       let a=arr[j]
        if(a==max)
        {
            console.log(arr[j])
            break;        
        }
        else{
            a=arr[j]+1
        }
    } 
}