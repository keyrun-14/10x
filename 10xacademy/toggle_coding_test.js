let fs = require("fs");
let data = fs.readFileSync("input.txt", 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}
// // -------- Do NOT edit anything above this line ----------
let s=readLine()
console.log(s)
let newstr=""
for(let i=0;i<s.length;i++){
    if(s[i]===s[i].toLowerCase()){
        newstr+=s[i].toUpperCase()
    }else{
        newstr+=s[i].toUpperCase()
    }
}
console.log(newstr)