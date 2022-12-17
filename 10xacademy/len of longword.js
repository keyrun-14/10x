let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');
function readLine() {
  idx++;
  return data[idx - 1];
}
// -------- Do NOT edit anything above this line ----------
let S=readLine().split();
let high=0;
for (let i=0;i<S.length;i++)
{
    if(S[i].length>high){
  high=S[i].length
  }
}
        console.log(high);