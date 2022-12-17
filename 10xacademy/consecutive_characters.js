let fs = require("fs");
let data = fs.readFileSync("input.txt", 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}
// // -------- Do NOT edit anything above this line ----------
let a=readLine();
let count=1
let b=[]
for(let i=0;i<a.length-1;i++){
   
    if(a[i]===a[i+1]){
        count=count+1
    }else{

    b.push(count)  
    count=1 
}
}
let temp=0;
for(let j=0;j<b.length;j++){
  if(temp<=b[j]){
    temp=b[j]
  }
}
console.log(temp)
