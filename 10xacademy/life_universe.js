let fs = require("fs");
let data = fs.readFileSync("input.txt", 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}
// // -------- Do NOT edit anything above this line ----------
do{
    let n=parseInt(readLine());
    if (n==42){
        break;
    }       
    else{
        console.log(n)
    }
}while (true);