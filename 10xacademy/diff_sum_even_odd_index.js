let fs = require("fs");
let data = fs.readFileSync("input.txt", 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}
// // -------- Do NOT edit anything above this line ----------
function difference_sum_even_odd_index(a,temp)
{
        for(let i=0;i<(a.length);i++)
        {
            if(i%2==0)
            {
                temp=temp+a[i]
            }
            else
            {
                temp=temp-a[i]
            }
        }console.log(temp);
} 

let a=readLine().split(" ").map( x => parseInt(x));
temp=0
difference_sum_even_odd_index(a,temp)