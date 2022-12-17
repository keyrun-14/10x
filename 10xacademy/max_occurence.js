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
let list=[]
let count=1
let maxx=-1
if(n>0)
{
    for(let i=0;i<n;i++)
{
    b=parseInt(readLine());
    list.push(b)
}
for(let i=0;i<n-1;i++)
{
    if(list[i]===list[i+1])
    {
        count=count+1
        maxx=Math.max(maxx,count)
        continue;       
    }
count=1
}
count=1
    for(let i=0;i<n-1;i++)
    {
        if(list[i]===list[i+1])
        {
            count=count+1
        }
       else
       {
           if(count==maxx)
           {
               console.log(list[i])
           }
           count=1
        } 
    }
    if(count==maxx)
    {
        console.log(list[n-1])
    } 
    if (maxx==-1)
    {
        console.log(-1)
    } 
}
else{
    console.log(-1)
}
