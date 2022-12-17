// let fs = require("fs");
// let data = fs.readFileSync("input.txt", 'utf-8');
// let idx = 0;
// data = data.split('\n');

// function readLine() {
//   idx++;
//   return data[idx - 1];
// }
// // // -------- Do NOT edit anything above this line ----------
// let p=parseInt(readLine());
// let t=parseInt(readLine());
// let r=parseInt(readLine());
// let si=(p*t*r)/100
// console.log(si)
a=["a","b","c","d"]
console.log(["start"]+a+["end"])
a.unshift("start")
a.push("end")
console.log(a)
console.log(["start"]+ a.slice(0)+["end"])