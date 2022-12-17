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
{
    for(let i=0;i<t;i++)
    {
        let n=parseInt(readLine());
        a = readLine().split(" ").map(x => parseInt(x));
        let sum=0
        for(let k=0;k<n;k++)
        {
            sum=sum+a[k]
        }
        let avg=sum/n
        let count=0
        for(let l=0;l<n;l++)
        {
            if (avg<a[l]){
                count=count+1
            }
        }console.log(count);
    }
}