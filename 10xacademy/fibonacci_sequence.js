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
let first_two=[0,1]
if(n<=0){
    console.log(-1)
}
else if (n===1){
    console.log(first_two[0])
}else if(n===2){
    console.log(first_two[0])
    console.log(first_two[1])
}
else{
        for(let i=0;i<n-2;i++){
            fibonacci=first_two[i]+first_two[i+1]
            first_two.push(fibonacci)
            }
for(let j=0;j<first_two.length;j++){
console.log(first_two[j])  
}
}