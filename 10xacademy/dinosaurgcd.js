let fs = require("fs");
let data = fs.readFileSync("input.txt", 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}
// // -------- Do NOT edit anything above this line ----------
// 
let t=parseInt(readLine());
for(let i=0;i<t;i++)
{
    let a=readLine().split(" ").map( x=> parseInt(x));
    let x1=a[0]
    let v1=a[1]
    let x2=a[2]
    let v2=a[3]
    let steps=(x2-x1)/(v1-v2)

       if((steps > 0) && (Number.isInteger(steps))==true)
        {
            console.log("YES")
        }
        else
        {
            console.log("NO")
        }
}


        // for (let i=1;i<=v1 && i<=v2;i++)
        // {
        //     if( v1%i==0 && v2%i==0)
        //     {
        //         hcf = i;
        //     }
        // }
        // lcm=(v1*v2)/hcf