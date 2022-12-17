// let fs = require("fs");
// const { arrayBuffer } = require("stream/consumers");
// let data = fs.readFileSync("input.txt", 'utf-8');
// let idx = 0;
// data = data.split('\n');

// function readLine() {
//   idx++;
//   return data[idx - 1];
// }
// // // -------- Do NOT edit anything above this line ----------

// let n=parseInt(readLine());
// let arr=[];
// for(let i=0;i<n;i++)
// {
//     arr.push(parseInt(readLine()));
// }
// arr.sort(function(a, b){return a - b});
// let count=1;
// let maxx=0;
// let required=0;
// for(let j=0;j<n-1;j++)
// {
//     if (arr[j]==arr[j+1])
//     {
//         count+=1;
//     }
//     else{
//         if (maxx<count)
//         {
//             maxx=count;
//             required=arr[j];
//             count=1
//         }
//     }
// }
// if (arr[-2]!=arr[-1])
//     {
//         maxx=count;
//             required=arr[-2];
//             count=1
//     }
// if (count==1)
// {   
//     console.log(Math.max(...arr))
// }
// else{
//     console.log(required)
// }
a=5;
console.log(a)
var a;
()=>{
    var a =7;
}