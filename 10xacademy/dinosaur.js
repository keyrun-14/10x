let fs = require("fs");
let data = fs.readFileSync("input.txt", 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}
// // -------- Do NOT edit anything above this line ----------
let t=parseInt(readLine());
for(let i=0;i<t;i++)
{
    let a=readLine().split(" ").map( x=> parseInt(x));
    let x1=a[0]
    let v1=a[1]
    let x2=a[2]
    let v2=a[3]
    let steps=(x1-x2)%(v2-v1)
    //for(let steps=0;steps<=10000;steps++)
    //{
        
       // if((x1+v1*steps === x2+v2*steps) && (v1>v2))
       if((steps === 0) && (v1>v2))
        {
            console.log("yes")
            //console.log(x1+v1*steps)
            //break;
        }
        else
        {
            console.log("No")
        }
    //}
/