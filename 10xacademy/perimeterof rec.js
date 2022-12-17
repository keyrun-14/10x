let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}

// -------- Do NOT edit anything above this line ----------
let l=parseInt(readLine());
let b=parseInt(readLine());
if (l>0 && b>0)
{
    console.log(2*(l+b));
}
else{
    console.log(0);
}