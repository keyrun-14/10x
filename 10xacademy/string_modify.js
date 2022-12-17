let fs = require("fs");
let data = fs.readFileSync("input.txt", 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}
// // -------- Do NOT edit anything above this line ----------
function String_modify(a,n) {    
    let newString = "";
    for (let i=0; i < a.length; i++) {
        a[0] = a[0].charAt(0).toUpperCase()  + a[i].slice(1);    
        if(newString[newString.length-1]==="."){
            newString+=" "+a[i].charAt(0).toUpperCase()  + a[i].slice(1); 
            continue;
        }
       if (a[i][0]===a[i][0].toUpperCase() && i>0){
        newString+=". "
       }  
       newString+=" "+a[i]
    }
    newString=newString.trim()
    if (newString[newString.length-1]!="."){
        newString+="."
    }
    return newString
}
let n=(readLine());
let a=n.split(" ")
let result = String_modify(a,n);
console.log(result);